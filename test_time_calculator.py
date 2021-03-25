import unittest
from time_calculator import *
from datetime import datetime, timedelta
import time


class UnitTests(unittest.TestCase):
    def test_get_time_from_str(self):
        time_str = "3:30 PM"
        actual = get_time_from_str(time_str)
        expected = datetime(1900, 1, 1, 15, 30)
        self.assertEqual(
            actual, expected,
            'Expected calling "get_time_from_str" with "3:30 PM"')

    def test_get_hours_from_str(self):
        hours_str = "1:30"
        actual = get_hours_from_str(hours_str)
        expected = timedelta(hours=1.5)
        self.assertEqual(actual, expected)

    def test_calculate_time(self):
        base_time = datetime(1900, 1, 1, 15, 30)
        hours = timedelta(hours=1.5)
        actual = calculate_time(base_time, hours)
        expected = datetime(1900, 1, 1, 17, 00)
        self.assertEqual(actual, expected)
