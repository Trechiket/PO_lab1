import unittest
from math import pi, sin, sqrt


class SinFunctionTestCase(unittest.TestCase):
    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0.0)

    def test_sin_pi_half(self):
        self.assertAlmostEqual(sin(pi / 2), 1.0)

    def test_sin_pi(self):
        self.assertAlmostEqual(sin(pi), 0.0)

    def test_sin_three_pi_half(self):
        self.assertAlmostEqual(sin(3 * pi / 2), -1.0)

    def test_sin_two_pi(self):
        self.assertAlmostEqual(sin(2 * pi), 0.0)

    def test_sin_pi_divide_four(self):
        self.assertAlmostEqual(sin(pi / 4), sqrt(2)/2)

    def test_sin_pi_divide_six(self):
        self.assertAlmostEqual(sin(pi / 6), 0.5)

    def test_sin_pi_divide_three(self):
        self.assertAlmostEqual(sin(pi / 3), sqrt(3)/2)
