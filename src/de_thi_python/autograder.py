"""Cham diem tu dong hai bo de Python trong thu muc bai nop.

Luu y: cong cu nay thuc thi truc tiep file .py cua bai nop. Chi cham cac file
ban tin cay va khong chay bai nop cua nguoi khac tren may co du lieu nhay cam.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any


EXAMS: dict[str, dict[str, Any]] = {
    "1": {
        "title": "De 1 - Ca 7g30",
        "default_folder": "HOTEN_MSSV",
        "questions": [
            {
                "number": 1,
                "stdin": "135\n",
                "checks": [
                    {
                        "name": "Dem chu so le cua 135 cho ket qua 3",
                        "points": 1.0,
                        "pattern": r"(so luong chu so le|dem chu so le)[^\n]{0,50}\b3\b",
                    },
                    {
                        "name": "Tinh S voi n = 135, ket qua xap xi 2.7431",
                        "points": 1.0,
                        "pattern": r"\bs\s*=\s*2[.,]74",
                    },
                ],
            },
            {
                "number": 2,
                "stdin": "AbC123\n",
                "checks": [
                    {
                        "name": "Dem duoc 2 ky tu viet hoa",
                        "points": 0.7,
                        "pattern": r"(so ky tu chu hoa|dem chu hoa)[^\n]{0,50}\b2\b",
                    },
                    {
                        "name": "Nhan dien chuoi khong doi xung",
                        "points": 0.6,
                        "pattern": r"(chuoi khong doi xung|\bfalse\b)",
                    },
                    {
                        "name": "Tinh tong chu so bang 6",
                        "points": 0.7,
                        "pattern": r"(tong cac chu so|tong chu so)[^\n]{0,50}\b6\b",
                    },
                ],
            },
            {
                "number": 3,
                "stdin": "2\n4\n-2\n3\n4\n0\n4\n",
                "checks": [
                    {
                        "name": "Tinh tong cac so duong chan bang 10",
                        "points": 1.0,
                        "pattern": r"tong cac so duong chan[^\n]{0,60}\b10\b",
                    },
                    {
                        "name": "Dem so 4 xuat hien 2 lan",
                        "points": 1.0,
                        "pattern": r"(so lan xuat hien cua 4 la|4 xuat hien 2 lan|dem.*\b4\b[^\n]{0,30}\b2\b)",
                    },
                ],
            },
            {
                "number": 4,
                "stdin": "1\nS001\nPython Co Ban\nNguyen Van A\nNXB Tre\n2020\nS001\n",
                "checks": [
                    {"name": "Luu ma sach S001", "points": 0.3, "pattern": r"s001"},
                    {"name": "Luu ten sach", "points": 0.4, "pattern": r"python co ban"},
                    {"name": "Luu ten tac gia", "points": 0.3, "pattern": r"nguyen van a"},
                    {"name": "Luu nha xuat ban", "points": 0.3, "pattern": r"nxb tre"},
                    {"name": "Luu nam xuat ban 2020", "points": 0.2, "pattern": r"\b2020\b"},
                    {"name": "Thong bao xoa sach thanh cong", "points": 0.3, "pattern": r"da duoc xoa"},
                    {
                        "name": "Ma S001 khong con trong tu dien sau khi xoa",
                        "points": 0.2,
                        "pattern": r"s001",
                        "section_after": "danh sach sach sau khi xu ly",
                        "should_match": False,
                    },
                ],
            },
            {
                "number": 5,
                "stdin": "",
                "checks": [
                    {"name": "Tao dien thoai DT01 va DT02", "points": 0.4, "pattern": r"dt01[\s\S]*dt02"},
                    {"name": "Dung ten may iPhone 15 Pro", "points": 0.4, "pattern": r"iphone 15 pro"},
                    {"name": "Dung hang Apple va Samsung", "points": 0.4, "pattern": r"apple[\s\S]*samsung"},
                    {"name": "Dung dung luong pin 3274 va 5000", "points": 0.4, "pattern": r"3274[\s\S]*5000"},
                    {"name": "Dung gia ban cua hai dien thoai", "points": 0.4, "pattern": r"28990000[\s\S]*29990000"},
                ],
            },
        ],
    },
    "2": {
        "title": "De 2 - Ca 9g45",
        "default_folder": "HOTEN_MSSV_DE_2",
        "questions": [
            {
                "number": 1,
                "stdin": "4\n",
                "checks": [
                    {
                        "name": "Tong uoc so cua 4 bang 7",
                        "points": 1.0,
                        "pattern": r"tong cac uoc so[^\n]{0,50}\b7\b",
                    },
                    {
                        "name": "Tinh S voi n = 4 bang 288",
                        "points": 1.0,
                        "pattern": r"\bs\s*=\s*288\b",
                    },
                ],
            },
            {
                "number": 2,
                "stdin": "Abc DE 12\n",
                "checks": [
                    {
                        "name": "Dem duoc 2 ky tu viet thuong",
                        "points": 0.7,
                        "pattern": r"(so ky tu chu thuong|dem chu thuong)[^\n]{0,50}\b2\b",
                    },
                    {
                        "name": "Nhan dien chuoi khong doi xung",
                        "points": 0.6,
                        "pattern": r"(chuoi khong doi xung|\bfalse\b)",
                    },
                    {
                        "name": "Viet hoa chu cai dau moi tu",
                        "points": 0.7,
                        "pattern": r"abc de 12",
                    },
                ],
            },
            {
                "number": 3,
                "stdin": "2\n4\n-2\n3\n4\n6\n0\n4\n",
                "checks": [
                    {
                        "name": "Loc dung danh sach so duong chan [2, 4, 4, 6]",
                        "points": 1.0,
                        "pattern": r"\[\s*2\s*,\s*4\s*,\s*4\s*,\s*6\s*\]",
                    },
                    {
                        "name": "Dem so 4 xuat hien 2 lan",
                        "points": 1.0,
                        "pattern": r"(4 xuat hien 2 lan|4[^\n]{0,30}2 lan|dem.*\b4\b[^\n]{0,30}\b2\b)",
                    },
                ],
            },
            {
                "number": 4,
                "stdin": "1\nPC01\n16\n512\nDell\n2023\nPC01\n",
                "checks": [
                    {"name": "Luu so hieu PC01", "points": 0.3, "pattern": r"pc01"},
                    {"name": "Luu dung luong bo nho 16", "points": 0.3, "pattern": r"\b16\b"},
                    {"name": "Luu dung luong o cung 512", "points": 0.3, "pattern": r"\b512\b"},
                    {"name": "Luu hang Dell va nam 2023", "points": 0.4, "pattern": r"dell[\s\S]*\b2023\b"},
                    {"name": "Thong bao xoa may tinh thanh cong", "points": 0.4, "pattern": r"da duoc xoa"},
                    {
                        "name": "PC01 khong con trong tu dien sau khi xoa",
                        "points": 0.3,
                        "pattern": r"pc01",
                        "section_after": "danh sach sau khi xu ly",
                        "should_match": False,
                    },
                ],
            },
            {
                "number": 5,
                "stdin": "",
                "checks": [
                    {"name": "Tao ma mon hoc 229008 va 224604", "points": 0.4, "pattern": r"229008[\s\S]*224604"},
                    {"name": "Dung ten Co so du lieu va Tieng Anh 1", "points": 0.4, "pattern": r"co so du lieu[\s\S]*tieng anh 1"},
                    {"name": "Dung so tin chi 3 va 2", "points": 0.4, "pattern": r"so tin chi[\s\S]*3[\s\S]*so tin chi[\s\S]*2"},
                    {"name": "Dung khoa Cong nghe thong tin", "points": 0.4, "pattern": r"cong nghe thong tin"},
                    {"name": "Dung khoa Ngoai ngu", "points": 0.4, "pattern": r"ngoai ngu"},
                ],
            },
        ],
    },
}


def _normalize(text: str) -> str:
    """Bo dau tieng Viet de viec doi chieu khong phu thuoc font chu."""
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFD", text)
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    return text.lower()


def _check_output(output: str, check: dict[str, Any]) -> bool:
    """Kiem tra mot tieu chi tren toan bo output hoac phan sau mot moc."""
    target = _normalize(output)
    marker = check.get("section_after")

    if marker:
        marker_normalized = _normalize(marker)
        if marker_normalized not in target:
            return False
        target = target.split(marker_normalized, 1)[1]

    found = re.search(check["pattern"], target, flags=re.IGNORECASE) is not None
    return found if check.get("should_match", True) else not found


def _run_submission(script: Path, test_input: str, timeout: float) -> tuple[str, str | None]:
    """Chay mot file bai nop va tra ve stdout, hoac thong bao loi."""
    try:
        completed = subprocess.run(
            [sys.executable, str(script.resolve())],
            input=test_input,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=timeout,
            cwd=str(script.parent),
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "", f"Qua thoi gian cho phep ({timeout:g} giay)."
    except OSError as error:
        return "", f"Khong the chay file: {error}"

    if completed.returncode != 0:
        detail = completed.stderr.strip() or f"Chuong trinh ket thuc voi ma loi {completed.returncode}."
        return completed.stdout, detail[-1200:]

    return completed.stdout, None


def grade_exam(exam: str, folder: str | Path, timeout: float = 5.0) -> dict[str, Any]:
    """Cham 5 file Cau1.py ... Cau5.py, moi cau toi da 2 diem."""
    exam = str(exam)
    if exam not in EXAMS:
        raise ValueError("Ma de phai la 1 hoac 2.")

    submission_dir = Path(folder).expanduser().resolve()
    if not submission_dir.is_dir():
        raise FileNotFoundError(f"Khong tim thay thu muc bai nop: {submission_dir}")

    exam_config = EXAMS[exam]
    question_results = []
    total_score = 0.0

    for question in exam_config["questions"]:
        number = question["number"]
        script = submission_dir / f"Cau{number}.py"
        check_results = []
        error = None
        output = ""

        if not script.is_file():
            error = f"Thieu file {script.name}."
        else:
            output, error = _run_submission(script, question["stdin"], timeout)

        for check in question["checks"]:
            passed = error is None and _check_output(output, check)
            earned = float(check["points"]) if passed else 0.0
            total_score += earned
            check_results.append(
                {
                    "name": check["name"],
                    "passed": passed,
                    "points": float(check["points"]),
                    "earned": earned,
                }
            )

        question_score = sum(item["earned"] for item in check_results)
        question_results.append(
            {
                "question": number,
                "score": round(question_score, 2),
                "max_score": 2.0,
                "error": error,
                "checks": check_results,
            }
        )

    return {
        "exam": exam,
        "exam_title": exam_config["title"],
        "folder": str(submission_dir),
        "graded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "score": round(total_score, 2),
        "max_score": 10.0,
        "questions": question_results,
    }


def save_report(report: dict[str, Any]) -> Path:
    """Luu ket qua cham diem thanh JSON trong thu muc reports/."""
    project_root = Path(__file__).resolve().parents[2]
    report_dir = project_root / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = report_dir / f"cham_diem_de_{report['exam']}_{timestamp}.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def print_report(report: dict[str, Any]) -> None:
    """In bang diem va chi tiet tieu chi dat/chua dat."""
    print("\n" + "=" * 62)
    print(f"AUTO CHAM DIEM - {report['exam_title']}")
    print(f"Thu muc: {report['folder']}")
    print("=" * 62)

    for question in report["questions"]:
        print(f"\nCau {question['question']}: {question['score']:.2f}/{question['max_score']:.2f} diem")
        if question["error"]:
            print(f"  LOI: {question['error']}")
        for check in question["checks"]:
            status = "DAT" if check["passed"] else "CHUA DAT"
            print(
                f"  [{status}] {check['name']} "
                f"({check['earned']:.2f}/{check['points']:.2f})"
            )

    print("\n" + "-" * 62)
    print(f"TONG DIEM: {report['score']:.2f}/10.00")
    print("=" * 62)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Tu dong cham bai thi Python - De 1 va De 2.")
    parser.add_argument("--de", choices=("1", "2"), help="Chon de 1 hoac de 2.")
    parser.add_argument("--folder", help="Duong dan thu muc chua Cau1.py den Cau5.py.")
    parser.add_argument("--timeout", type=float, default=5.0, help="Thoi gian toi da cho moi cau (giay).")
    args = parser.parse_args(argv)

    exam = args.de
    if exam is None:
        print("CHON DE CAN CHAM")
        print("1. De 1 - Ca 7g30")
        print("2. De 2 - Ca 9g45")
        exam = input("Nhap de (1/2): ").strip()
        if exam not in EXAMS:
            print("Lua chon khong hop le.")
            return 2

    default_folder = EXAMS[exam]["default_folder"]
    folder_value = args.folder
    if folder_value is None:
        folder_value = input(f"Thu muc bai nop [{default_folder}]: ").strip() or default_folder

    if args.timeout <= 0:
        print("Timeout phai lon hon 0.")
        return 2

    try:
        report = grade_exam(exam, folder_value, timeout=args.timeout)
    except (FileNotFoundError, ValueError) as error:
        print(f"Loi: {error}")
        return 2

    print_report(report)
    report_path = save_report(report)
    print(f"\nDa luu bao cao JSON: {report_path}")
    print("Luu y: bo cham thuc thi file Python bai nop. Chi chay ma nguon ban tin cay.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
