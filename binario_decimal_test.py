from parameterized import parameterized, parameterized_class
import unittest
from binario_decimal import dec2bin, bin2dec

class bi2de(unittest.TestCase):
    @parameterized.expand([
        ("01011100",92),
    ])
    def test(self, bin, dec):
        self.assertEqual(bin2dec(bin),dec)

class de2bi(unittest.TestCase):
    @parameterized.expand([
        (97,"01100001"),
        (25, "00011001")
    ])
    def test(self, dec, bin):
        self.assertEqual(dec2bin(dec),bin)



if __name__ == '__main__':
    unittest.main()