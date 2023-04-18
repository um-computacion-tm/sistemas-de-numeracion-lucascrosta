from parameterized import parameterized, parameterized_class
import unittest
from octal_decimal import dec2oct, oct2dec

class de2oc(unittest.TestCase):
    @parameterized.expand([
        (92,134),
        (737,1341)
    ])
    def test(self, dec, oct):
        self.assertEqual(dec2oct(dec),oct)

class oc2de(unittest.TestCase):
    @parameterized.expand([
        (141,97),
        (31,25)
    ])
    def test(self, oct, dec):
        self.assertEqual(oct2dec(oct),dec)



if __name__ == '__main__':
    unittest.main()