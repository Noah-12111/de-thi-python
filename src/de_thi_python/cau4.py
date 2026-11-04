"""Cau 4: Quan ly thong tin sach bang tu dien."""

from datetime import datetime
from typing import Dict, List, Union

# Moi ma sach la mot key; gia tri la danh sach thong tin cua sach.
ThongTinSach = List[Union[str, int]]
TuDienSach = Dict[str, ThongTinSach]


def them_sach(
    tu_dien: TuDienSach,
    ma_so: str,
    ten_sach: str,
    ten_tac_gia: str,
    nha_xuat_ban: str,
    nam_xuat_ban: int,
) -> None:
    """Them mot cuon sach vao tu dien."""
    if not ma_so.strip():
        raise ValueError("Ma so sach khong duoc de trong.")

    if ma_so in tu_dien:
        raise ValueError("Ma so sach da ton tai.")

    nam_hien_tai = datetime.now().year
    if nam_xuat_ban < 0 or nam_xuat_ban > nam_hien_tai:
        raise ValueError("Nam xuat ban khong hop le.")

    tu_dien[ma_so] = [
        ten_sach,
        ten_tac_gia,
        nha_xuat_ban,
        nam_xuat_ban,
    ]


def xoa_sach(tu_dien: TuDienSach, ma_so: str) -> bool:
    """Xoa sach theo ma. Tra ve True neu xoa thanh cong."""
    if ma_so in tu_dien:
        del tu_dien[ma_so]
        return True

    return False


def hien_thi_sach(tu_dien: TuDienSach) -> None:
    """In danh sach sach trong tu dien."""
    if not tu_dien:
        print("Thu vien chua co sach.")
        return

    print("\nDANH SACH SACH")
    for ma_so, thong_tin in tu_dien.items():
        print("Ma sach:", ma_so)
        print("Ten sach:", thong_tin[0])
        print("Tac gia:", thong_tin[1])
        print("Nha xuat ban:", thong_tin[2])
        print("Nam xuat ban:", thong_tin[3])
        print("-" * 30)


def main() -> None:
    """Chay chuong trinh cau 4."""
    tu_dien: TuDienSach = {}

    while True:
        try:
            n = int(input("Nhap so luong sach can them (n > 0): "))
            if n > 0:
                break
            print("So luong sach phai lon hon 0.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    for i in range(n):
        print("\nNhap thong tin sach thu", i + 1)

        while True:
            ma_so = input("Nhap ma so sach: ").strip()
            if ma_so and ma_so not in tu_dien:
                break
            print("Ma sach khong duoc trong va khong duoc trung.")

        ten_sach = input("Nhap ten sach: ").strip()
        ten_tac_gia = input("Nhap ten tac gia: ").strip()
        nha_xuat_ban = input("Nhap nha xuat ban: ").strip()

        while True:
            try:
                nam_xuat_ban = int(input("Nhap nam xuat ban: "))
                if 0 <= nam_xuat_ban <= datetime.now().year:
                    break
                print("Nam xuat ban khong hop le.")
            except ValueError:
                print("Vui long nhap nam bang so nguyen.")

        them_sach(
            tu_dien,
            ma_so,
            ten_sach,
            ten_tac_gia,
            nha_xuat_ban,
            nam_xuat_ban,
        )

    hien_thi_sach(tu_dien)

    ma_can_xoa = input("\nNhap ma so sach can xoa: ").strip()
    if xoa_sach(tu_dien, ma_can_xoa):
        print("Cuon sach co ma so", ma_can_xoa, "da duoc xoa.")
    else:
        print("Khong tim thay cuon sach can xoa.")

    print("\nDanh sach sau khi xu ly:")
    hien_thi_sach(tu_dien)


if __name__ == "__main__":
    main()
