# Cau truc project

Project duoc to chuc theo mo hinh **src layout**. Ma nguon package nam trong `src/de_thi_python/`, tach rieng tung bai thanh module.

## So do

```text
de-thi-python/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .vscode/
│   └── settings.json
├── docs/
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
```

## Vai tro tung thanh phan

| Thanh phan | Chuc nang |
|---|---|
| `src/de_thi_python/` | Python package chinh cua du an |
| `cau1.py` den `cau5.py` | Moi file la mot module giai mot cau |
| `__init__.py` | Danh dau thu muc la package va khai bao phien ban |
| `__main__.py` | Cho phep chay package bang `python -m de_thi_python` |
| `cli.py` | Menu dong lenh de chon bai |
| `tests/` | Cac unit test kiem tra ham va lop |
| `HOTEN_MSSV/` | 5 file Python doc lap de nop bai theo de |
| `pyproject.toml` | Khai bao metadata, Python version, package va lenh CLI |
| `.github/workflows/` | Tu dong chay kiem thu khi push/pull request |
| `docs/` | Tai lieu cau truc va huong dan |
| `.gitignore` | Bo qua file tam, cache, moi truong ao |
| `.editorconfig` | Thong nhat dinh dang ma nguon |

## Quan he giua module va package

- **Module** la mot file Python, vi du `cau1.py`.
- **Package** la mot thu muc gom cac module Python va co file `__init__.py`, vi du `de_thi_python`.
- **CLI** la giao dien dong lenh, duoc module `cli.py` quan ly.
- **Unit test** la cac bai kiem tra nho de dam bao ham tra ve ket qua dung.

## Luong chay

```text
Nguoi dung
    |
    v
__main__.py
    |
    v
cli.py (menu)
    |
    +--> cau1.py
    +--> cau2.py
    +--> cau3.py
    +--> cau4.py
    +--> cau5.py
```

Cac module bai tap co the duoc import va tai su dung trong module khac hoac trong unit test.
