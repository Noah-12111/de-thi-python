"""Kiem thu bo cham diem tu dong."""

import unittest
from pathlib import Path

from de_thi_python.autograder import _check_output, _normalize, grade_exam


class TestAutoGrader(unittest.TestCase):
    def test_normalize_tieng_viet(self):
        self.assertEqual(_normalize("Đề thi Python"), "de thi python")

    def test_check_output_co_the_kiem_tra_phan_sau_khi_xoa(self):
        check = {
            "pattern": r"s001",
            "section_after": "Danh sach sau khi xu ly",
            "should_match": False,
        }
        self.assertTrue(_check_output("S001 da xoa\nDanh sach sau khi xu ly\n{}", check))
        self.assertFalse(_check_output("S001 da xoa\nDanh sach sau khi xu ly\n{'S001': []}", check))

    def test_cham_duoc_de_1_mau(self):
        project_root = Path(__file__).resolve().parents[1]
        report = grade_exam("1", project_root / "HOTEN_MSSV")
        self.assertEqual(report["score"], 10.0)

    def test_cham_duoc_de_2_mau(self):
        project_root = Path(__file__).resolve().parents[1]
        report = grade_exam("2", project_root / "HOTEN_MSSV_DE_2")
        self.assertEqual(report["score"], 10.0)


if __name__ == "__main__":
    unittest.main()
