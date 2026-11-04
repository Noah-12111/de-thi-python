# Tai lieu on tap nhanh

## De 1 - Ca 7g30

### Cau 1 - So nguyen va ham
- `%`: lay phan du de lay chu so cuoi.
- `//`: chia lay phan nguyen de bo chu so cuoi.
- `while`: lap den khi so khong con chu so.
- Dem chu so le va tinh S = 1/2 + 1/4 + ... + 1/(2*n).

### Cau 2 - Chuoi
- `isupper()`: kiem tra ky tu viet hoa.
- `isdigit()`: kiem tra ky tu so.
- `s[::-1]`: dao nguoc chuoi.
- `s == s[::-1]`: kiem tra doi xung.

### Cau 3 - Danh sach
- `[]`: tao danh sach rong.
- `append(x)`: them phan tu.
- `break`: ket thuc vong lap khi nhap 0.
- So duong chan: `x > 0 and x % 2 == 0`.

### Cau 4 - Tu dien sach
- `{}`: tao tu dien.
- Ma sach la key, thong tin sach la value.
- `in`: kiem tra key.
- `del`: xoa sach theo ma.

### Cau 5 - DienThoai
- `class`: khai bao lop.
- `__init__()`: khoi tao doi tuong.
- `self`: doi tuong hien tai.

## De 2 - Ca 9g45

### Cau 1 - Uoc so va luy thua
- Duyet `i` tu 1 den `n`.
- Neu `n % i == 0`, i la uoc so cua n.
- Cong cac uoc so de tinh tong.
- Cong `i ** i` de tinh S = 1 + 2^2 + 3^3 + ... + n^n.
- n nam trong doan [1; 99].

### Cau 2 - Xu ly chuoi
- `islower()`: kiem tra ky tu chu thuong.
- `s == s[::-1]`: kiem tra chuoi doi xung.
- `s.title()`: viet hoa ky tu dau moi tu.

### Cau 3 - Danh sach
- Nhap so nguyen den khi nhap 0.
- So duong chan: `i > 0 and i % 2 == 0`.
- `list.count(k)`: dem so lan xuat hien cua k.

### Cau 4 - Tu dien may tinh
- `{}`: tao tu dien.
- So hieu may tinh la key.
- Value gom bo nho, o cung, hang san xuat va nam san xuat.
- `del dict[so_hieu]`: xoa may tinh theo so hieu.

### Cau 5 - MonHoc
- Tao lop `MonHoc`.
- Thuoc tinh: `MaMonHoc`, `TenMonHoc`, `SoTinChi`, `KhoaPhuTrach`.
- `__init__()`: khoi tao thong tin mon hoc.
- `thongtinmonhoc()`: hien thi thong tin mon hoc.
- Tao hai doi tuong theo du lieu trong de.
