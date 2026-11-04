# Cau truc project

Project su dung mo hinh **src layout**. Bai tap duoc chia thanh module va package theo tung de thi; bo unit test duoc tach rieng trong hai thu muc De_1 va De_2.

## So do tong quat

~~~text
de-thi-python/
├── .github/workflows/python-tests.yml
├── docs/
│   ├── ON_TAP.md
│   └── PROJECT_STRUCTURE.md
├── HOTEN_MSSV/                  # 5 file nop bai cua De 1
├── HOTEN_MSSV_DE_2/             # 5 file nop bai cua De 2
├── src/
│   └── de_thi_python/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py               # Menu chon de va cau hoi
│       ├── cau1.py              # De 1 - Cau 1
│       ├── cau2.py              # De 1 - Cau 2
│       ├── cau3.py              # De 1 - Cau 3
│       ├── cau4.py              # De 1 - Cau 4
│       ├── cau5.py              # De 1 - Cau 5
│       └── de_2/
│           ├── __init__.py
│           ├── cau1.py
│           ├── cau2.py
│           ├── cau3.py
│           ├── cau4.py
│           └── cau5.py
├── tests/
│   ├── __init__.py
│   ├── De_1/
│   │   ├── __init__.py
│   │   ├── test_cau1.py
│   │   ├── test_cau2.py
│   │   ├── test_cau3.py
│   │   ├── test_cau4.py
│   │   └── test_cau5.py
│   └── De_2/
│       ├── __init__.py
│       ├── test_cau1.py
│       ├── test_cau2.py
│       ├── test_cau3.py
│       ├── test_cau4.py
│       └── test_cau5.py
├── .editorconfig
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
~~~

## 1. Module va package

- **Module** la mot file Python, vi du `cau1.py`.
- **Package** la thu muc gom nhieu module va co file `__init__.py`.
- Package goc `de_thi_python` chua loi giai De 1.
- Package con `de_thi_python.de_2` chua loi giai De 2.
- `cli.py` la giao dien dong lenh de chon de thi va chay tung cau.

## 2. Bo kiem thu

Thu muc `tests` duoc chia theo de thi:

| Thu muc | Noi dung |
|---|---|
| `tests/De_1/` | Unit test cho 5 cau cua De 1 |
| `tests/De_2/` | Unit test cho 5 cau cua De 2 |

Moi file `test_cauN.py` kiem tra cac ham hoac lop tuong ung trong package source. Hai bo test duoc chay chung bang lenh:

~~~bash
python -m unittest discover -s tests -v
~~~

Co the chay rieng tung de:

~~~bash
python -m unittest discover -s tests/De_1 -v
python -m unittest discover -s tests/De_2 -v
~~~

## 3. Thanh phan cau hinh

| Thanh phan | Chuc nang |
|---|---|
| `pyproject.toml` | Metadata, dependency va cau hinh build package |
| `.gitignore` | Bo qua cache, moi truong ao va file build |
| `.editorconfig` | Thong nhat dinh dang ma nguon |
| `.vscode/settings.json` | Thiet lap co ban cho VS Code |
| `.github/workflows/` | Chay unit test tu dong tren GitHub Actions |
| `docs/` | Tai lieu cau truc va noi dung on tap |
| `HOTEN_MSSV/` | File nop bai De 1 |
| `HOTEN_MSSV_DE_2/` | File nop bai De 2 |

## 4. Luong chay

~~~text
Nguoi dung
    |
    v
__main__.py
    |
    v
cli.py
    |
    +---- Chon De 1 ----> Module cau1.py ... cau5.py
    |
    +---- Chon De 2 ----> Package de_2/cau1.py ... cau5.py
~~~
