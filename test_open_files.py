"""Test open_file.py."""

import open_files
import unittest

class test_open_files(unittest.TestCase):
    """Test cases."""

    def test_open_files(self):
        """Test the 'open_files.open_file' method."""
        self.assertEqual(open_files.open_file('starts/design.in'), [(12, 12), (13, 32), (43, 23)])