# Đề thi Python — Project ôn tập và thực hành

[![Python tests](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml)

Project giải đề thi kết thúc môn **Lập trình Python (mã môn 229152, mã đề 11301)**. Source được tổ chức thành Python package có module, CLI, kiểm thử tự động và tài liệu. Repository đồng thời giữ 5 file Python độc lập theo cấu trúc nộp bài của đề thi.

## 1. Mục tiêu

- Giải đầy đủ 5 câu theo đề và đáp án mẫu được cung cấp.
- Dùng cú pháp Python cơ bản, tên hàm dễ hiểu và chú thích rõ ràng.
- Tách mỗi câu thành một module để import và tái sử dụng.
- Gom các module vào một package.
- Có menu CLI để chạy chương trình.
- Có unit test để kiểm tra hàm và lớp.
- Có cấu hình đóng gói bằng pyproject.toml và GitHub Actions.

## 2. Công nghệ

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.10 trở lên |
| Package/build | setuptools, pyproject.toml |
| Giao diện | Command Line Interface (CLI) |
| Kiểm thử | unittest (thư viện chuẩn Python) |
| Quản lý mã nguồn | Git và GitHub |
| Tự động kiểm thử | GitHub Actions |
| IDE | Visual Studio Code |

Không cần thư viện bên thứ ba cho chức năng bài tập. Sau khi cài package editable, có thể import package từ thư mục src.

## 3. Cấu trúc project

~~~text
de-thi-python/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .vscode/
│   └── settings.json
├── docs/
│   ├── ON_TAP.md
│   └── PROJECT_STRUCTURE.md
├── HOTEN_MSSV/
│   ├── Cau1.py
│   ├── Cau2.py
│   ├── Cau3.py
│   ├── Cau4.py
│   └── Cau5.py
├── src/
│   └── de_thi_python/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── cau1.py
│       ├── cau2.py
│       ├── cau3.py
│       ├── cau4.py
│       └── cau5.py
├── tests/
│   ├── __init__.py
│   ├── test_cau1.py
│   ├── test_cau2.py
│   ├── test_cau3.py
│   ├── test_cau4.py
│   └── test_cau5.py
├── .editorconfig
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
~~~

### Vai trò các thành phần

| Thành phần | Vai trò |
|---|---|
| src/de_thi_python/ | Package chứa mã nguồn chính |
| cau1.py đến cau5.py | Năm module giải năm câu |
| __init__.py | Khởi tạo package và khai báo phiên bản |
| __main__.py | Cho phép chạy package bằng python -m de_thi_python |
| cli.py | Menu chọn câu hỏi |
| tests/ | Unit test cho các module |
| HOTEN_MSSV/ | Năm file độc lập theo định dạng nộp bài |
| pyproject.toml | Metadata, phiên bản Python, cấu hình build và lệnh CLI |
| .github/workflows/ | Tự động kiểm thử khi push hoặc tạo pull request |
| docs/ | Tài liệu cấu trúc và ôn tập |

Xem thêm: [Tài liệu cấu trúc project](docs/PROJECT_STRUCTURE.md) và [Tài liệu ôn tập](docs/ON_TAP.md).

## 4. Cài đặt project

### Bước 1: Tải source

Clone repository:

~~~bash
git clone https://github.com/Noah-12111/de-thi-python.git
cd de-thi-python
~~~

Hoặc tải [ZIP của repository](https://github.com/Noah-12111/de-thi-python/archive/refs/heads/main.zip), giải nén và mở thư mục bằng VS Code.

### Bước 2: Tạo môi trường ảo (khuyến nghị)

Windows PowerShell:

~~~powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
~~~

Linux/macOS:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

### Bước 3: Cài đặt package

Tại thư mục gốc project, chạy:

~~~bash
python -m pip install -e .
~~~

Tham số -e cài package ở chế độ editable. Khi sửa source trong src/de_thi_python, không cần cài đặt lại sau mỗi lần thay đổi.

## 5. Cách chạy chương trình

### Cách 1 — Chạy menu tổng

~~~bash
python -m de_thi_python
~~~

Sau khi cài đặt, có thể thử dùng lệnh:

~~~bash
de-thi-python
~~~

Menu cho phép chọn câu 1 đến câu 5 và quay lại menu sau khi chạy.

### Cách 2 — Chạy riêng từng module

~~~bash
python -m de_thi_python.cau1
python -m de_thi_python.cau2
python -m de_thi_python.cau3
python -m de_thi_python.cau4
python -m de_thi_python.cau5
~~~

### Cách 3 — Chạy file nộp bài độc lập

Windows PowerShell:

~~~powershell
py .\HOTEN_MSSV\Cau1.py
py .\HOTEN_MSSV\Cau2.py
py .\HOTEN_MSSV\Cau3.py
py .\HOTEN_MSSV\Cau4.py
py .\HOTEN_MSSV\Cau5.py
~~~

Các file trong HOTEN_MSSV không phụ thuộc package src, vì vậy có thể chạy độc lập.

## 6. Nội dung năm module

### Câu 1 — Số nguyên và hàm

File: src/de_thi_python/cau1.py

- Kiểm tra n thuộc đoạn từ 1 đến 1500.
- dem_chu_so_le(n): đếm chữ số lẻ.
- tinh_s(n): tính S = 1/2 + 1/4 + ... + 1/(2*n).

Ví dụ: n = 635 thì có 2 chữ số lẻ (3 và 5).

### Câu 2 — Xử lý chuỗi

File: src/de_thi_python/cau2.py

- dem_chu_hoa(s): đếm ký tự viết hoa bằng isupper().
- la_chuoi_doi_xung(s): so sánh chuỗi với s[::-1].
- tinh_tong_chu_so(s): cộng các ký tự số trong chuỗi.

Ví dụ: AbcA21 có 2 ký tự viết hoa, không đối xứng và tổng chữ số bằng 3.

### Câu 3 — Danh sách

File: src/de_thi_python/cau3.py

- Nhập các số nguyên đến khi người dùng nhập 0.
- tong_so_duong_chan(danh_sach): tính tổng số dương chẵn.
- dem_so_lan_xuat_hien(danh_sach, k): đếm số lần xuất hiện của k.

### Câu 4 — Từ điển quản lý sách

File: src/de_thi_python/cau4.py

- Sử dụng dictionary với mã sách làm key.
- Thông tin sách được lưu trong value.
- them_sach(...): thêm sách và kiểm tra mã trùng.
- xoa_sach(...): xóa sách theo mã và trả về True/False.
- hien_thi_sach(...): hiển thị danh sách sách.

### Câu 5 — Lập trình hướng đối tượng

File: src/de_thi_python/cau5.py

- Khai báo lớp DienThoai.
- Các thuộc tính: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.
- __init__() khởi tạo đối tượng.
- thongtindienthoai() hiển thị thông tin.
- Tạo hai đối tượng mẫu theo đúng dữ liệu đề thi.

## 7. Chạy kiểm thử

Project sử dụng unittest, đã có sẵn trong Python, không cần cài pytest.

~~~bash
python -m unittest discover -s tests -v
~~~

Các test kiểm tra:
- Đếm chữ số lẻ và tính tổng S.
- Đếm chữ hoa, chuỗi đối xứng và tổng chữ số.
- Tổng số dương chẵn và đếm phần tử.
- Thêm/xóa sách và xử lý mã sách trùng.
- Tạo đối tượng DienThoai và dữ liệu mẫu.

GitHub Actions tự chạy bộ test trên Python 3.10, 3.11, 3.12 và 3.13 khi có push lên main hoặc pull request.

## 8. Định dạng nộp bài

Đề thi yêu cầu một thư mục tên theo mẫu HOTEN_MSSV chứa 5 file .py.

Trước khi nộp:
1. Đổi tên thư mục HOTEN_MSSV thành họ tên và mã số sinh viên của bạn.
2. Kiểm tra đủ Cau1.py đến Cau5.py.
3. Chạy thử từng file độc lập.
4. Chỉ nộp thư mục 5 file theo yêu cầu giảng viên, trừ khi giảng viên yêu cầu nộp toàn bộ project.

## 9. Thông tin project

- Repository: [Noah-12111/de-thi-python](https://github.com/Noah-12111/de-thi-python)
- Phiên bản: 1.0.0
- License: MIT
