"""Cau 4 - Quan ly thong tin sach bang tu dien."""

from datetime import datetime


def main():
    n = int(input("Nhap so luong sach can them (n > 0): "))
    while n <= 0:
        print("So luong sach phai lon hon 0. Vui long nhap lai!")
        n = int(input("Nhap so luong sach (n > 0): "))

    tu_dien = {}
    nam_hien_tai = datetime.now().year

    for i in range(n):
        print("\nNhap thong tin sach thu", i + 1)
        ma_so_sach = input("Nhap ma so sach: ")
        ten_sach = input("Nhap ten sach: ")
        ten_tac_gia = input("Nhap ten tac gia: ")
        nha_xuat_ban = input("Nhap nha xuat ban: ")

        nam_xuat_ban = int(input("Nhap nam xuat ban: "))
        while nam_xuat_ban > nam_hien_tai:
            print("Nam xuat ban khong hop le. Nam phai <=", nam_hien_tai)
            nam_xuat_ban = int(input("Nhap lai nam xuat ban: "))

        # Moi ma so sach la mot khoa; thong tin sach duoc luu trong list.
        tu_dien[ma_so_sach] = [
            ten_sach,
            ten_tac_gia,
            nha_xuat_ban,
            nam_xuat_ban
        ]

    print("\nDanh sach sach trong thu vien:")
    print(tu_dien)

    # Tim ma so sach va xoa neu ma so ton tai.
    ma_can_xoa = input("\nNhap ma so sach can xoa: ")
    if ma_can_xoa in tu_dien:
        del tu_dien[ma_can_xoa]
        print("Cuon sach co ma so", ma_can_xoa, "da duoc xoa.")
    else:
        print("Khong tim thay cuon sach can xoa.")

    print("Danh sach sach sau khi xu ly:")
    print(tu_dien)


if __name__ == "__main__":
    main()
