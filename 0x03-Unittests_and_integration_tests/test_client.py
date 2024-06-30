#!/usr/bin/env python3
"""testing client class"""
from unittest import TestCase, mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """test class for Github Org"""

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @mock.patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """test org"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(expected)
