"""De 2 - Cau 4: Quan ly thong tin may tinh bang tu dien."""

from typing import Dict, List, Union

ThongTinMayTinh = List[Union[str, int]]
TuDienMayTinh = Dict[str, ThongTinMayTinh]


def them_may_tinh(
    tu_dien: TuDienMayTinh,
    so_hieu: str,
    bo_nho: int,
    o_cung: int,
    hang_san_xuat: str,
    nam_san_xuat: int,
) -> None:
    """Them thong tin mot may tinh vao tu dien."""
    if not so_hieu.strip():
        raise ValueError("So hieu may tinh khong duoc de trong.")

    if so_hieu in tu_dien:
        raise ValueError("So hieu may tinh da ton tai.")

    tu_dien[so_hieu] = [
        bo_nho,
        o_cung,
        hang_san_xuat,
        nam_san_xuat,
    ]


def xoa_may_tinh(tu_dien: TuDienMayTinh, so_hieu: str) -> bool:
    """Xoa may tinh theo so hieu. Tra ve True neu xoa thanh cong."""
    if so_hieu in tu_dien:
        del tu_dien[so_hieu]
        return True

    return False


def hien_thi_may_tinh(tu_dien: TuDienMayTinh) -> None:
    """Hien thi danh sach may tinh."""
    if not tu_dien:
        print("Danh sach may tinh dang trong.")
        return

    for so_hieu, thong_tin in tu_dien.items():
        print("So hieu:", so_hieu)
        print("Dung luong bo nho:", thong_tin[0])
        print("Dung luong o cung:", thong_tin[1])
        print("Hang san xuat:", thong_tin[2])
        print("Nam san xuat:", thong_tin[3])
        print("-" * 30)


def main() -> None:
    """Chay chuong trinh De 2 - Cau 4."""
    tu_dien: TuDienMayTinh = {}

    while True:
        try:
            n = int(input("Nhap so luong may tinh: "))
            if n > 0:
                break
            print("So luong phai lon hon 0.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    for i in range(n):
        print("\nNhap thong tin may tinh thu", i + 1)

        while True:
            so_hieu = input("Nhap so hieu may tinh: ").strip()
            if so_hieu and so_hieu not in tu_dien:
                break
            print("So hieu khong duoc trong va khong duoc trung.")

        bo_nho = int(input("Nhap dung luong bo nho: "))
        o_cung = int(input("Nhap dung luong o cung: "))
        hang_san_xuat = input("Nhap hang san xuat: ").strip()
        nam_san_xuat = int(input("Nhap nam san xuat: "))

        them_may_tinh(
            tu_dien,
            so_hieu,
            bo_nho,
            o_cung,
            hang_san_xuat,
            nam_san_xuat,
        )

    print("\nDanh sach may tinh:")
    hien_thi_may_tinh(tu_dien)

    ma_can_xoa = input("Nhap so hieu may tinh can xoa: ").strip()
    if xoa_may_tinh(tu_dien, ma_can_xoa):
        print("May tinh co so hieu", ma_can_xoa, "da duoc xoa.")
    else:
        print("Khong co may tinh can tim.")

    print("\nDanh sach sau khi xu ly:")
    hien_thi_may_tinh(tu_dien)


if __name__ == "__main__":
    main()
