"""Giao dien dong lenh chon de thi va cau hoi."""

from . import autograder, cau1, cau2, cau3, cau4, cau5
from .de_2 import (
    cau1 as de2_cau1,
    cau2 as de2_cau2,
    cau3 as de2_cau3,
    cau4 as de2_cau4,
    cau5 as de2_cau5,
)


DE_1 = {
    "1": ("Cau 1 - So nguyen va ham", cau1.main),
    "2": ("Cau 2 - Xu ly chuoi", cau2.main),
    "3": ("Cau 3 - Danh sach", cau3.main),
    "4": ("Cau 4 - Tu dien quan ly sach", cau4.main),
    "5": ("Cau 5 - Lop DienThoai", cau5.main),
}

DE_2 = {
    "1": ("Cau 1 - Tong uoc so va tinh S", de2_cau1.main),
    "2": ("Cau 2 - Chuoi va viet hoa dau moi tu", de2_cau2.main),
    "3": ("Cau 3 - Danh sach so duong chan", de2_cau3.main),
    "4": ("Cau 4 - Tu dien quan ly may tinh", de2_cau4.main),
    "5": ("Cau 5 - Lop MonHoc", de2_cau5.main),
}


def chay_menu_cau_hoi(ten_de: str, cac_chuc_nang: dict) -> None:
    """Hien thi menu cau hoi va chay cau duoc chon."""
    while True:
        print("\n" + "=" * 52)
        print("                 " + ten_de)
        print("=" * 52)

        for lua_chon, (ten_cau, _) in cac_chuc_nang.items():
            print(lua_chon + ". " + ten_cau)

        print("0. Quay lai menu chon de")
        print("=" * 52)

        lua_chon = input("Nhap lua chon: ").strip()

        if lua_chon == "0":
            return

        chuc_nang = cac_chuc_nang.get(lua_chon)

        if chuc_nang is None:
            print("Lua chon khong hop le. Vui long chon tu 0 den 5.")
            continue

        ten_cau, ham_chay = chuc_nang
        print("\n--- " + ten_cau + " ---")
        ham_chay()
        input("\nNhan Enter de quay lai menu...")


def main() -> int:
    """Menu chinh cho phep chon De 1 hoac De 2."""
    while True:
        print("\n" + "=" * 52)
        print("        CHUONG TRINH ON TAP LAP TRINH PYTHON")
        print("=" * 52)
        print("1. De 1 - De thi ca 7g30")
        print("2. De 2 - De thi ca 9g45")
        print("3. Auto cham diem bai nop")
        print("0. Thoat chuong trinh")
        print("=" * 52)

        lua_chon = input("Chon de thi: ").strip()

        if lua_chon == "0":
            print("Cam on ban da su dung chuong trinh.")
            return 0
        if lua_chon == "1":
            chay_menu_cau_hoi("DE 1", DE_1)
        elif lua_chon == "2":
            chay_menu_cau_hoi("DE 2", DE_2)
        elif lua_chon == "3":
            autograder.main()
        else:
            print("Lua chon khong hop le. Vui long chon 0, 1, 2 hoac 3.")


if __name__ == "__main__":
    raise SystemExit(main())
