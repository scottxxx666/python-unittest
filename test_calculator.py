from unittest import TestCase, mock

from calculator import add


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))

    def test_get_random(self):
        fake = mock.Mock()
        fake.return_value = 3
        with mock.patch('calculator.random', fake):
            from calculator import get_random
            self.assertEqual(3, get_random())
