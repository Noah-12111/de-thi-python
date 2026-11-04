import unittest

from de_thi_python.de_2.cau4 import them_may_tinh, xoa_may_tinh


class TestDe2Cau4(unittest.TestCase):
    def setUp(self):
        self.tu_dien = {}

    def test_them_va_xoa_may_tinh(self):
        them_may_tinh(self.tu_dien, "PC001", 16, 512, "Dell", 2023)
        self.assertIn("PC001", self.tu_dien)
        self.assertEqual(self.tu_dien["PC001"], [16, 512, "Dell", 2023])
        self.assertTrue(xoa_may_tinh(self.tu_dien, "PC001"))
        self.assertNotIn("PC001", self.tu_dien)

    def test_xoa_ma_khong_ton_tai(self):
        self.assertFalse(xoa_may_tinh(self.tu_dien, "PC999"))

    def test_khong_cho_phep_trung_so_hieu(self):
        them_may_tinh(self.tu_dien, "PC001", 8, 256, "HP", 2022)
        with self.assertRaises(ValueError):
            them_may_tinh(self.tu_dien, "PC001", 16, 512, "Dell", 2023)


if __name__ == "__main__":
    unittest.main()
