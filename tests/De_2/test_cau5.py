import unittest

from de_thi_python.de_2.cau5 import MonHoc, tao_du_lieu_mau


class TestDe2Cau5(unittest.TestCase):
    def test_tao_doi_tuong(self):
        mon_hoc = MonHoc(229008, "Co so du lieu", 3, "Cong nghe thong tin")
        self.assertEqual(mon_hoc.MaMonHoc, 229008)
        self.assertEqual(mon_hoc.TenMonHoc, "Co so du lieu")
        self.assertEqual(mon_hoc.SoTinChi, 3)
        self.assertEqual(mon_hoc.KhoaPhuTrach, "Cong nghe thong tin")

    def test_du_lieu_mau(self):
        danh_sach = tao_du_lieu_mau()
        self.assertEqual(len(danh_sach), 2)
        self.assertEqual(danh_sach[0].MaMonHoc, 229008)
        self.assertEqual(danh_sach[1].MaMonHoc, 224604)


if __name__ == "__main__":
    unittest.main()
