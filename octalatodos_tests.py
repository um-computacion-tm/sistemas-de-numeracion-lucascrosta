from parameterized import parameterized, parameterized_class
import unittest
from octalatodos import oct2dec, oct2hex, oct2bin

class oc2de(unittest.TestCase):
    @parameterized.expand([
        (141,97),
        (31,25)
    ])
    def test(self, oct, dec):
        self.assertEqual(oct2dec(oct),dec)

class oc2he(unittest.TestCase):
    @parameterized.expand([
        (135,"5D"),
        (31,"19")
    ])
    def test(self, oct, hex):
        self.assertEqual(oct2hex(oct),hex)

class oc2bi(unittest.TestCase):
    @parameterized.expand([
        (135,"001011101"),
        (31,"011001")
    ])
    def test(self, oct, bin):
        self.assertEqual(oct2bin(oct),bin)



if __name__ == '__main__':
    unittest.main()