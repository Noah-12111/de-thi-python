"""Cau 2: Xu ly chuoi ky tu."""


def dem_chu_hoa(s: str) -> int:
    """Dem so ky tu viet hoa trong chuoi."""
    dem = 0

    for ky_tu in s:
        if ky_tu.isupper():
            dem += 1

    return dem


def la_chuoi_doi_xung(s: str) -> bool:
    """Kiem tra chuoi co doc xuoi va nguoc giong nhau hay khong."""
    return s == s[::-1]


def tinh_tong_chu_so(s: str) -> int:
    """Tinh tong cac ky tu chu so trong chuoi."""
    tong = 0

    for ky_tu in s:
        if ky_tu.isdigit():
            tong += int(ky_tu)

    return tong


def main() -> None:
    """Chay chuong trinh cau 2."""
    s = input("Nhap chuoi s: ")

    so_chu_hoa = dem_chu_hoa(s)
    if so_chu_hoa == 0:
        print("Chuoi khong co ky tu chu hoa.")
    else:
        print("So ky tu chu hoa:", so_chu_hoa)

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Tong cac chu so trong chuoi:", tinh_tong_chu_so(s))


if __name__ == "__main__":
    main()
