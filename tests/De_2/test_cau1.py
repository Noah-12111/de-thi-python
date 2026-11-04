import unittest

from de_thi_python.de_2.cau1 import tong_uoc_so, tinh_s


class TestDe2Cau1(unittest.TestCase):
    def test_tong_uoc_so(self):
        self.assertEqual(tong_uoc_so(12), 28)
        self.assertEqual(tong_uoc_so(7), 8)
        self.assertEqual(tong_uoc_so(1), 1)

    def test_tinh_s(self):
        self.assertEqual(tinh_s(1), 1)
        self.assertEqual(tinh_s(2), 5)
        self.assertEqual(tinh_s(3), 32)

    def test_n_khong_hop_le(self):
        with self.assertRaises(ValueError):
            tong_uoc_so(0)


if __name__ == "__main__":
    unittest.main()
