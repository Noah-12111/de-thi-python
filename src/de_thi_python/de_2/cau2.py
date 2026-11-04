"""De 2 - Cau 2: Xu ly chuoi ky tu."""


def dem_chu_thuong(s: str) -> int:
    """Dem so ky tu chu thuong trong chuoi."""
    dem = 0

    for ky_tu in s:
        if ky_tu.islower():
            dem += 1

    return dem


def la_chuoi_doi_xung(s: str) -> bool:
    """Kiem tra chuoi co doi xung hay khong."""
    return s == s[::-1]


def viet_hoa_dau_moi_tu(s: str) -> str:
    """Viet hoa ky tu dau tien cua moi tu bang title()."""
    return s.title()


def main() -> None:
    """Chay chuong trinh De 2 - Cau 2."""
    s = input("Nhap chuoi s: ")

    so_chu_thuong = dem_chu_thuong(s)
    if so_chu_thuong == 0:
        print("Chuoi khong co ky tu chu thuong.")
    else:
        print("So ky tu chu thuong trong chuoi:", so_chu_thuong)

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Chuoi sau khi viet hoa ky tu dau moi tu:", viet_hoa_dau_moi_tu(s))


if __name__ == "__main__":
    main()
