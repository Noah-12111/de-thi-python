import unittest

from de_thi_python.cau4 import them_sach, xoa_sach


class TestDe1Cau4(unittest.TestCase):
    def setUp(self):
        self.tu_dien = {}

    def test_them_va_xoa_sach(self):
        them_sach(self.tu_dien, "S001", "Python co ban", "Nguyen Van A", "NXB Tre", 2020)
        self.assertIn("S001", self.tu_dien)
        self.assertEqual(self.tu_dien["S001"][0], "Python co ban")
        self.assertTrue(xoa_sach(self.tu_dien, "S001"))
        self.assertNotIn("S001", self.tu_dien)

    def test_xoa_ma_khong_ton_tai(self):
        self.assertFalse(xoa_sach(self.tu_dien, "KHONG_CO"))

    def test_khong_cho_phep_trung_ma(self):
        them_sach(self.tu_dien, "S001", "Sach A", "Tac gia", "NXB", 2020)
        with self.assertRaises(ValueError):
            them_sach(self.tu_dien, "S001", "Sach B", "Tac gia", "NXB", 2021)


if __name__ == "__main__":
    unittest.main()
