#!/usr/bin/env python3
"""testing utils for github org client"""
from parameterized import parameterized
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """testing access_nested_map function"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """testing access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """testing access_nested_map function"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """testing get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """testing get_json function"""
        config = {'return_value.json.return_value': test_payload}
        patcher = mock.patch('requests.get', **config)
        mock_get = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once()
        patcher.stop()


class TestMemoize(TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            val_1 = test_class.a_property()
            val_2 = test_class.a_property()
            self.assertEqual(val_1, val_2)
            mock_a_method.assert_called_once()
