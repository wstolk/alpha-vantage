import unittest
import os

from alpha_vantage import Client


class ClientTestCase(unittest.TestCase):
    def test_valid_key(self):
        self.assertIsInstance(Client("123456789abcdefg"), Client)

    def test_invalid_key(self):
        with self.assertRaises(ValueError): Client("")

    def test_no_key(self):
        with self.assertRaises(TypeError): Client()
