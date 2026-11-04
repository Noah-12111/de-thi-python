# De thi Python — Project on tap va thuc hanh

[![Python tests](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Noah-12111/de-thi-python/actions/workflows/python-tests.yml)

Project giai hai de thi thuc hanh mon **Lap trinh Python (ma mon 229152)**. Moi de co 5 cau, duoc to chuc thanh module va package rieng; unit test duoc tach trong hai thu muc `tests/De_1` va `tests/De_2`.

## 1. Hai de thi trong repository

| Bo de | Tep PDF | Noi dung |
|---|---|---|
| De 1 | Ca 7g30 | So nguyen, chuoi, danh sach, tu dien quan ly sach, lop DienThoai |
| De 2 | Ca 9g45 | Uoc so va luy thua, chuoi, danh sach so duong chan, tu dien may tinh, lop MonHoc |

## 2. Cau truc project

~~~text
de-thi-python/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   ├── ON_TAP.md
│   └── PROJECT_STRUCTURE.md
├── HOTEN_MSSV/                 # 5 file nop bai cua De 1
│   ├── Cau1.py
│   ├── Cau2.py
│   ├── Cau3.py
│   ├── Cau4.py
│   └── Cau5.py
├── HOTEN_MSSV_DE_2/            # 5 file nop bai cua De 2
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
│       ├── cau1.py ... cau5.py
│       └── de_2/
│           ├── __init__.py
│           └── cau1.py ... cau5.py
├── tests/
│   ├── __init__.py
│   ├── De_1/
│   │   ├── __init__.py
│   │   └── test_cau1.py ... test_cau5.py
│   └── De_2/
│       ├── __init__.py
│       └── test_cau1.py ... test_cau5.py
├── .editorconfig
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
~~~

**Quan trong:** Test duoc phan tach theo de, khong de chung mot cap file test:
- `tests/De_1/`: kiem thu 5 cau cua De 1.
- `tests/De_2/`: kiem thu 5 cau cua De 2.

Ma nguon tuong ung:
- `src/de_thi_python/cau1.py` den `cau5.py`: loi giai De 1.
- `src/de_thi_python/de_2/cau1.py` den `cau5.py`: loi giai De 2.

## 3. Cong nghe

| Thanh phan | Cong nghe |
|---|---|
| Ngon ngu | Python 3.10 tro len |
| Package/build | setuptools, pyproject.toml |
| Giao dien | CLI (menu dong lenh) |
| Kiem thu | unittest |
| CI | GitHub Actions |
| IDE | Visual Studio Code |

Khong can thu vien ben thu ba de chay cac bai tap va unit test.

## 4. Cai dat

Clone repository:

~~~bash
git clone https://github.com/Noah-12111/de-thi-python.git
cd de-thi-python
~~~

Tao moi truong ao (khuyen nghi):

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

Cai dat package:

~~~bash
python -m pip install -e .
~~~

## 5. Chay chuong trinh

Chay menu chinh:

~~~bash
python -m de_thi_python
~~~

Menu cho phep chon De 1 hoac De 2, sau do chon mot trong 5 cau.

Chay rieng module De 1:

~~~bash
python -m de_thi_python.cau1
python -m de_thi_python.cau2
python -m de_thi_python.cau3
python -m de_thi_python.cau4
python -m de_thi_python.cau5
~~~

Chay rieng module De 2:

~~~bash
python -m de_thi_python.de_2.cau1
python -m de_thi_python.de_2.cau2
python -m de_thi_python.de_2.cau3
python -m de_thi_python.de_2.cau4
python -m de_thi_python.de_2.cau5
~~~

## 6. Chay unit test

Chay tat ca test cua ca hai de:

~~~bash
python -m unittest discover -s tests -v
~~~

Chi chay test De 1:

~~~bash
python -m unittest discover -s tests/De_1 -v
~~~

Chi chay test De 2:

~~~bash
python -m unittest discover -s tests/De_2 -v
~~~

GitHub Actions tu dong cai dat package va chay test tren Python 3.10, 3.11, 3.12 va 3.13 moi khi co push hoac pull request.

## 7. File nop bai

De thi yeu cau mot folder ten theo mau `HOTEN_MSSV` chua dung 5 file `.py`.

- De 1: dung 5 file trong `HOTEN_MSSV/`.
- De 2: dung 5 file trong `HOTEN_MSSV_DE_2/`; khi nop, doi ten folder nay thanh `HOTEN_MSSV` neu giang vien yeu cau dung ten folder mau.
- Khong nop ca hai bo de trong cung mot folder neu de bai chi yeu cau mot folder 5 file.
- Cac file trong hai folder nop bai chay doc lap, khong can import package `src`.

## 8. Tai lieu

- [Cau truc project](docs/PROJECT_STRUCTURE.md)
- [Tu khoa on tap cho ca hai de](docs/ON_TAP.md)
- [Unit test va cach chay](tests/README.md)
- [GitHub Actions](https://github.com/Noah-12111/de-thi-python/actions)

## 9. Thong tin

- Repository: [Noah-12111/de-thi-python](https://github.com/Noah-12111/de-thi-python)
- Version: `1.0.0`
- Python: `>=3.10`
- License: MIT
