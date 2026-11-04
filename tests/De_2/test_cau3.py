import unittest

from de_thi_python.de_2.cau3 import dem_so_lan_xuat_hien, lay_so_duong_chan


class TestDe2Cau3(unittest.TestCase):
    def setUp(self):
        self.danh_sach = [2, 4, -2, 3, 4, 0, 6]

    def test_lay_so_duong_chan(self):
        self.assertEqual(lay_so_duong_chan(self.danh_sach), [2, 4, 4, 6])
        self.assertEqual(lay_so_duong_chan([-3, -2, 1, 3]), [])

    def test_dem_so_lan_xuat_hien(self):
        self.assertEqual(dem_so_lan_xuat_hien(self.danh_sach, 4), 2)
        self.assertEqual(dem_so_lan_xuat_hien(self.danh_sach, 99), 0)


if __name__ == "__main__":
    unittest.main()
