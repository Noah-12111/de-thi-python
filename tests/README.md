# Unit tests

Bo kiem thu duoc chia theo tung de thi de khong bi nham cau hoi giua hai bo de.

~~~text
tests/
├── __init__.py
├── test_autograder.py
├── De_1/
│   ├── __init__.py
│   ├── test_cau1.py
│   ├── test_cau2.py
│   ├── test_cau3.py
│   ├── test_cau4.py
│   └── test_cau5.py
└── De_2/
    ├── __init__.py
    ├── test_cau1.py
    ├── test_cau2.py
    ├── test_cau3.py
    ├── test_cau4.py
    └── test_cau5.py
~~~

## Chay tat ca test

~~~bash
python -m unittest discover -s tests -v
~~~

## Chi chay De 1

~~~bash
python -m unittest discover -s tests/De_1 -v
~~~

## Chi chay De 2

~~~bash
python -m unittest discover -s tests/De_2 -v
~~~

Moi bo test import module source tu `src/de_thi_python`. Vi vay, hay cai package truoc khi chay:

~~~bash
python -m pip install -e .
~~~

## Kiem thu bo cham diem tu dong

File `test_autograder.py` kiem tra viec chuan hoa tieng Viet, quy tac kiem tra ket qua sau thao tac xoa, va chay thu bo cham diem voi hai thu muc bai nop mau.

Chay cung cac test khac:

~~~bash
python -m unittest discover -s tests -v
~~~

