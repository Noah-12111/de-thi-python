"""Giao dien dong lenh de chon va chay tung cau hoi."""

from . import cau1, cau2, cau3, cau4, cau5


def hien_thi_menu() -> None:
    """Hien thi menu chinh."""
    print("\n" + "=" * 48)
    print("       CHUONG TRINH ON TAP LAP TRINH PYTHON")
    print("=" * 48)
    print("1. Cau 1 - So nguyen va ham")
    print("2. Cau 2 - Xu ly chuoi")
    print("3. Cau 3 - Danh sach")
    print("4. Cau 4 - Tu dien quan ly sach")
    print("5. Cau 5 - Lop va doi tuong DienThoai")
    print("0. Thoat chuong trinh")
    print("=" * 48)


def main() -> int:
    """Vong lap menu cua chuong trinh."""
    cac_chuc_nang = {
        "1": cau1.main,
        "2": cau2.main,
        "3": cau3.main,
        "4": cau4.main,
        "5": cau5.main,
    }

    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "0":
            print("Cam on ban da su dung chuong trinh.")
            return 0

        chuc_nang = cac_chuc_nang.get(lua_chon)

        if chuc_nang is None:
            print("Lua chon khong hop le. Vui long chon tu 0 den 5.")
            continue

        print()
        chuc_nang()

        input("\nNhan Enter de quay lai menu...")


if __name__ == "__main__":
    raise SystemExit(main())
