import unittest

from de_thi_python.de_2.cau2 import dem_chu_thuong, la_chuoi_doi_xung, viet_hoa_dau_moi_tu


class TestDe2Cau2(unittest.TestCase):
    def test_dem_chu_thuong(self):
        self.assertEqual(dem_chu_thuong("Abc DE 12"), 3)
        self.assertEqual(dem_chu_thuong("ABC123"), 0)

    def test_doi_xung(self):
        self.assertTrue(la_chuoi_doi_xung("radar"))
        self.assertFalse(la_chuoi_doi_xung("Python"))

    def test_viet_hoa_dau_moi_tu(self):
        self.assertEqual(viet_hoa_dau_moi_tu("lap trinh python"), "Lap Trinh Python")
        self.assertEqual(viet_hoa_dau_moi_tu("kHOA cong nghe"), "Khoa Cong Nghe")


if __name__ == "__main__":
    unittest.main()
