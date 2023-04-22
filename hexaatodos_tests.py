from parameterized import parameterized, parameterized_class
import unittest
from hexaatodos import hex2dec, hex2oct, hex2bin

class he2de(unittest.TestCase):
    @parameterized.expand([
        ("15C",348),
        ("2A",42)
    ])
    def test(self, hex, dec):
        self.assertEqual(hex2dec(hex),dec)

class he2oc(unittest.TestCase):
    @parameterized.expand([
        ("15C",534),
        ("2A",52)
    ])
    def test(self, hex, oct):
        self.assertEqual(hex2oct(hex),oct)

class he2bi(unittest.TestCase):
    @parameterized.expand([
        ("15C","000101011100"),
        ("2A","00101010")
    ])
    def test(self, hex, bin):
        self.assertEqual(hex2bin(hex),bin)



if __name__ == '__main__':
    unittest.main()