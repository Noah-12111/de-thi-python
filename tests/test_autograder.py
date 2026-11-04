"""Kiem thu bo cham diem tu dong."""

import shutil
import tempfile
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
        self.assertTrue(_check_output("S001 da xoa\\nDanh sach sau khi xu ly\\n{}", check))
        self.assertFalse(_check_output("S001 da xoa\\nDanh sach sau khi xu ly\\n{'S001': []}", check))

    def test_cham_duoc_de_1_mau(self):
        project_root = Path(__file__).resolve().parents[1]
        report = grade_exam("1", project_root / "HOTEN_MSSV")
        self.assertEqual(report["score"], 10.0)

    def test_cham_duoc_de_2_mau(self):
        project_root = Path(__file__).resolve().parents[1]
        report = grade_exam("2", project_root / "HOTEN_MSSV_DE_2")
        self.assertEqual(report["score"], 10.0)

    def test_bai_lam_de_1_thieu_cau_5_van_duoc_cham_diem_thanh_phan(self):
        project_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            submission_dir = Path(temp_dir)
            for question_number in range(1, 5):
                source = project_root / "HOTEN_MSSV" / f"Cau{question_number}.py"
                shutil.copy2(source, submission_dir / source.name)
            report = grade_exam("1", submission_dir)

        self.assertEqual(report["score"], 8.0)
        self.assertEqual([item["score"] for item in report["questions"]], [2.0, 2.0, 2.0, 2.0, 0.0])
        self.assertEqual(report["questions"][4]["error"], "Thieu file Cau5.py.")


if __name__ == "__main__":
    unittest.main()
