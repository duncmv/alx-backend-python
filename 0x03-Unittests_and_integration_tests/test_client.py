#!/usr/bin/env python3
"""testing client class"""
from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """test class for Github Org"""

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """test org"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(expected)

    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test = GithubOrgClient('test')
            result = test._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_b:

            mock_b.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in payload]
            self.assertEqual(result, check)

            mock_b.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
