import unittest

from de_thi_python.cau5 import DienThoai, tao_du_lieu_mau


class TestDe1Cau5(unittest.TestCase):
    def test_tao_doi_tuong(self):
        dien_thoai = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
        self.assertEqual(dien_thoai.MaMay, "DT01")
        self.assertEqual(dien_thoai.TenMay, "iPhone 15 Pro")
        self.assertEqual(dien_thoai.HangSanXuat, "Apple")
        self.assertEqual(dien_thoai.DungLuongPin, 3274)
        self.assertEqual(dien_thoai.GiaBan, 28990000)

    def test_du_lieu_mau(self):
        danh_sach = tao_du_lieu_mau()
        self.assertEqual(len(danh_sach), 2)
        self.assertEqual(danh_sach[0].MaMay, "DT01")
        self.assertEqual(danh_sach[1].MaMay, "DT02")


if __name__ == "__main__":
    unittest.main()
