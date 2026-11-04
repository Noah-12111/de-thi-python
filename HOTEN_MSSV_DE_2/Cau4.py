"""De 2 - Cau 4: Quan ly thong tin may tinh bang tu dien."""


def main():
    n = int(input("Nhap so luong may tinh: "))
    while n <= 0:
        n = int(input("Nhap lai so luong may tinh (n > 0): "))

    tu_dien = {}

    for i in range(n):
        print("\nNhap thong tin may tinh thu", i + 1)
        so_hieu = input("Nhap so hieu may tinh: ")
        bo_nho = int(input("Nhap dung luong bo nho: "))
        o_cung = int(input("Nhap dung luong o cung: "))
        hang_san_xuat = input("Nhap hang san xuat: ")
        nam_san_xuat = int(input("Nhap nam san xuat: "))

        tu_dien[so_hieu] = [
            bo_nho,
            o_cung,
            hang_san_xuat,
            nam_san_xuat
        ]

    print("\nDanh sach may tinh:")
    print(tu_dien)

    x = input("Nhap so hieu may tinh can xoa: ")
    if x in tu_dien:
        del tu_dien[x]
        print("May tinh co so hieu", x, "da duoc xoa.")
    else:
        print("Khong co may tinh can tim.")

    print("Danh sach sau khi xu ly:")
    print(tu_dien)


if __name__ == "__main__":
    main()
