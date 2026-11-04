import unittest

from de_thi_python.cau1 import dem_chu_so_le, tinh_s


class TestDe1Cau1(unittest.TestCase):
    def test_dem_chu_so_le(self):
        self.assertEqual(dem_chu_so_le(635), 2)
        self.assertEqual(dem_chu_so_le(2468), 0)
        self.assertEqual(dem_chu_so_le(13579), 5)

    def test_tinh_s(self):
        self.assertAlmostEqual(tinh_s(1), 0.5)
        self.assertAlmostEqual(tinh_s(2), 0.75)

    def test_n_khong_hop_le(self):
        with self.assertRaises(ValueError):
            tinh_s(0)


if __name__ == "__main__":
    unittest.main()
