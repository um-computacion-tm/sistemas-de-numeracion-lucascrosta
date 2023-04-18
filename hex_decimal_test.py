from parameterized import parameterized, parameterized_class
import unittest
from hex_decimal import hex2dec, dec2hex

class de2he(unittest.TestCase):
    @parameterized.expand([
        (92,"5C"),
        (10, "A"),
        (5,"5")
    ])
    def test(self, dec, hex):
        self.assertEqual(dec2hex(dec),hex)

class he2de(unittest.TestCase):
    @parameterized.expand([
        ("15C",348),
        ("2A",42)
    ])
    def test(self, hex, dec):
        self.assertEqual(hex2dec(hex),dec)



if __name__ == '__main__':
    unittest.main()