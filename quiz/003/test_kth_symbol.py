import unittest

from kth_symbol import kth_symbol


class TestKthSymbol(unittest.TestCase):

    def test_kth_symbol_n1_k1(self):
        self.assertEqual(kth_symbol(1, 1), 0, "kth_symbol(1, 1) should return 0")

    def test_kth_symbol_n2_k1(self):
        self.assertEqual(kth_symbol(2, 1), 0, "kth_symbol(2, 1) should return 0")

    def test_kth_symbol_n2_k2(self):
        self.assertEqual(kth_symbol(2, 2), 1, "kth_symbol(2, 2) should return 1")

    def test_kth_symbol_n3_k1(self):
        self.assertEqual(kth_symbol(3, 1), 0, "kth_symbol(3, 1) should return 0")

    def test_kth_symbol_n3_k2(self):
        self.assertEqual(kth_symbol(3, 2), 1, "kth_symbol(3, 2) should return 1")

    def test_kth_symbol_n3_k3(self):
        self.assertEqual(kth_symbol(3, 3), 1, "kth_symbol(3, 3) should return 1")

    def test_kth_symbol_n3_k4(self):
        self.assertEqual(kth_symbol(3, 4), 0, "kth_symbol(3, 4) should return 0")

    def test_kth_symbol_n4_k1(self):
        self.assertEqual(kth_symbol(4, 1), 0, "kth_symbol(4, 1) should return 0")

    def test_kth_symbol_n4_k2(self):
        self.assertEqual(kth_symbol(4, 2), 1, "kth_symbol(4, 2) should return 1")

    def test_kth_symbol_n4_k3(self):
        self.assertEqual(kth_symbol(4, 3), 1, "kth_symbol(4, 3) should return 1")

    def test_kth_symbol_n4_k4(self):
        self.assertEqual(kth_symbol(4, 4), 0, "kth_symbol(4, 4) should return 0")

    def test_kth_symbol_n4_k5(self):
        self.assertEqual(kth_symbol(4, 5), 1, "kth_symbol(4, 5) should return 1")

    def test_kth_symbol_n4_k6(self):
        self.assertEqual(kth_symbol(4, 6), 0, "kth_symbol(4, 6) should return 0")


if __name__ == "__main__":
    unittest.main()
