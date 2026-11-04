import unittest

from de_thi_python.cau3 import dem_so_lan_xuat_hien, tong_so_duong_chan


class TestDe1Cau3(unittest.TestCase):
    def setUp(self):
        self.danh_sach = [2, 4, -2, 3, 4, 0]

    def test_tong_so_duong_chan(self):
        self.assertEqual(tong_so_duong_chan(self.danh_sach), 10)

    def test_dem_so_lan_xuat_hien(self):
        self.assertEqual(dem_so_lan_xuat_hien(self.danh_sach, 4), 2)
        self.assertEqual(dem_so_lan_xuat_hien(self.danh_sach, 99), 0)


if __name__ == "__main__":
    unittest.main()
