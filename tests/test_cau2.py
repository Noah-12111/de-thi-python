import unittest

from de_thi_python.cau2 import (
    dem_chu_hoa,
    la_chuoi_doi_xung,
    tinh_tong_chu_so,
)


class TestCau2(unittest.TestCase):
    def test_dem_chu_hoa(self):
        self.assertEqual(dem_chu_hoa("AbC123"), 2)
        self.assertEqual(dem_chu_hoa("python"), 0)

    def test_chuoi_doi_xung(self):
        self.assertTrue(la_chuoi_doi_xung("radar"))
        self.assertFalse(la_chuoi_doi_xung("python"))

    def test_tong_chu_so(self):
        self.assertEqual(tinh_tong_chu_so("AbcA21"), 3)
        self.assertEqual(tinh_tong_chu_so("khong co so"), 0)


if __name__ == "__main__":
    unittest.main()
