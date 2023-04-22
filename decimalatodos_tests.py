from parameterized import parameterized, parameterized_class
import unittest
from decimalatodos import dec2bin, dec2oct, dec2hex

class de2bi(unittest.TestCase):
    @parameterized.expand([
        (97,"01100001"),
        (25, "00011001")
    ])
    def test(self, dec, bin):
        self.assertEqual(dec2bin(dec),bin)

class de2oc(unittest.TestCase):
    @parameterized.expand([
        (92,134),
        (737,1341)
    ])
    def test(self, dec, oct):
        self.assertEqual(dec2oct(dec),oct)

class de2he(unittest.TestCase):
    @parameterized.expand([
        (92,"5C"),
        (10, "A"),
        (5,"5")
    ])
    def test(self, dec, hex):
        self.assertEqual(dec2hex(dec),hex)



if __name__ == '__main__':
    unittest.main()