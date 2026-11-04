# De thi Python — Project on tap va thuc hanh

[![Python tests](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml)

Project giai de thi ket thuc mon **Lap trinh Python (ma mon 229152, ma de 11301)**. Source duoc to chuc thanh Python package co module, CLI, kiem thu tu dong va tai lieu. Repository dong thoi giu 5 file Python doc lap theo cau truc nop bai cua de thi.

## 1. Muc tieu

- Giai day du 5 cau theo de va dap an mau duoc cung cap.
- Dung cu phap Python co ban, ten ham de hieu va chu thich ro rang.
- Tach moi cau thanh mot module de import va tai su dung.
- Gom cac module vao mot package.
- Co menu CLI de chay chuong trinh.
- Co unit test de kiem tra ham va lop.
- Co cau hinh dong goi bang pyproject.toml va GitHub Actions.

## 2. Cong nghe

| Thanh phan | Cong nghe |
|---|---|
| Ngon ngu | Python 3.9 tro len |
| Package/build | setuptools, pyproject.toml |
| Giao dien | Command Line Interface (CLI) |
| Kiem thu | unittest (thu vien chuan Python) |
| Quan ly ma nguon | Git va GitHub |
| Tu dong kiem thu | GitHub Actions |
| IDE | Visual Studio Code |

Khong can thu vien ben thu ba cho cac chuc nang bai tap. Sau khi cai package editable, co the import package tu thu muc src.

## 3. Cau truc project

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
├── pyproject.toml
└── README.md
~~~

### Vai tro cac thanh phan

| Thanh phan | Vai tro |
|---|---|
| src/de_thi_python/ | Package chua ma nguon chinh |
| cau1.py den cau5.py | Nam module giai nam cau |
| __init__.py | Khoi tao package va khai bao phien ban |
| __main__.py | Cho phep chay package bang python -m de_thi_python |
| cli.py | Menu chon cau hoi |
| tests/ | Unit test cho cac module |
| HOTEN_MSSV/ | Nam file doc lap theo dinh dang nop bai |
| pyproject.toml | Metadata, phien ban Python, cau hinh build va lenh CLI |
| .github/workflows/ | Tu dong kiem thu khi push hoac tao pull request |
| docs/ | Tai lieu cau truc va on tap |

Xem them: [Tai lieu cau truc project](docs/PROJECT_STRUCTURE.md).

## 4. Cai dat project

### Buoc 1: Tai source

Clone repository:

~~~bash
git clone https://github.com/Noah-12111/de-thi-python.git
cd de-thi-python
~~~

Hoac tai [ZIP cua repository](https://github.com/Noah-12111/de-thi-python/archive/refs/heads/main.zip), giai nen va mo thu muc bang VS Code.

### Buoc 2: Tao moi truong ao (khuyen nghi)

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

### Buoc 3: Cai dat package

Tai thu muc goc project, chay:

~~~bash
python -m pip install -e .
~~~

Tham so -e cai package o che do editable. Khi sua source trong src/de_thi_python, khong can cai dat lai sau moi lan thay doi.

## 5. Cach chay chuong trinh

### Cach 1 — Chay menu tong

~~~bash
python -m de_thi_python
~~~

Sau khi cai dat, co the thu dung lenh:

~~~bash
de-thi-python
~~~

Menu cho phep chon cau 1 den cau 5 va quay lai menu sau khi chay.

### Cach 2 — Chay rieng tung module

~~~bash
python -m de_thi_python.cau1
python -m de_thi_python.cau2
python -m de_thi_python.cau3
python -m de_thi_python.cau4
python -m de_thi_python.cau5
~~~

### Cach 3 — Chay file nop bai doc lap

Windows PowerShell:

~~~powershell
py .\HOTEN_MSSV\Cau1.py
py .\HOTEN_MSSV\Cau2.py
py .\HOTEN_MSSV\Cau3.py
py .\HOTEN_MSSV\Cau4.py
py .\HOTEN_MSSV\Cau5.py
~~~

Cac file trong HOTEN_MSSV khong phu thuoc package src, vi vay co the chay doc lap.

## 6. Noi dung nam module

### Cau 1 — So nguyen va ham

File: src/de_thi_python/cau1.py

- Kiem tra n thuoc doan tu 1 den 1500.
- dem_chu_so_le(n): dem chu so le.
- tinh_s(n): tinh S = 1/2 + 1/4 + ... + 1/(2*n).

Vi du: n = 635 thi co 2 chu so le (3 va 5).

### Cau 2 — Xu ly chuoi

File: src/de_thi_python/cau2.py

- dem_chu_hoa(s): dem ky tu viet hoa bang isupper().
- la_chuoi_doi_xung(s): so sanh chuoi voi s[::-1].
- tinh_tong_chu_so(s): cong cac ky tu so trong chuoi.

Vi du: AbcA21 co 2 ky tu viet hoa, khong doi xung va tong chu so bang 3.

### Cau 3 — Danh sach

File: src/de_thi_python/cau3.py

- Nhap cac so nguyen den khi nguoi dung nhap 0.
- tong_so_duong_chan(danh_sach): tinh tong so duong chan.
- dem_so_lan_xuat_hien(danh_sach, k): dem so lan xuat hien cua k.

### Cau 4 — Tu dien quan ly sach

File: src/de_thi_python/cau4.py

- Su dung dictionary voi ma sach lam key.
- Thong tin sach duoc luu trong value.
- them_sach(...): them sach va kiem tra ma trung.
- xoa_sach(...): xoa sach theo ma va tra ve True/False.
- hien_thi_sach(...): hien thi danh sach sach.

### Cau 5 — Lap trinh huong doi tuong

File: src/de_thi_python/cau5.py

- Khai bao lop DienThoai.
- Cac thuoc tinh: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.
- __init__() khoi tao doi tuong.
- thongtindienthoai() hien thi thong tin.
- Tao hai doi tuong mau theo dung du lieu de thi.

## 7. Chay kiem thu

Project su dung unittest, da co san trong Python, khong can cai pytest.

~~~bash
python -m unittest discover -s tests -v
~~~

Cac test kiem tra:
- Dem chu so le va tinh tong S.
- Dem chu hoa, chuoi doi xung va tong chu so.
- Tong so duong chan va dem phan tu.
- Them/xoa sach va xu ly ma sach trung.
- Tao doi tuong DienThoai va du lieu mau.

GitHub Actions tu chay bo test khi co push len main hoac pull request.

## 8. Dinh dang nop bai

De thi yeu cau mot thu muc ten theo mau HOTEN_MSSV chua 5 file .py.

Truoc khi nop:
1. Doi ten thu muc HOTEN_MSSV thanh ho ten va ma so sinh vien cua ban.
2. Kiem tra du Cau1.py den Cau5.py.
3. Chay thu tung file doc lap.
4. Chi nop thu muc 5 file theo yeu cau giang vien, tru khi giang vien yeu cau nop toan bo project.

## 9. Thong tin project

- Repository: [Noah-12111/de-thi-python](https://github.com/Noah-12111/de-thi-python)
- Phien ban: 1.0.0
- License: MIT
