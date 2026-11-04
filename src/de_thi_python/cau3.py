"""Cau 3: Nhap va xu ly danh sach so nguyen."""


def tong_so_duong_chan(danh_sach: list[int]) -> int:
    """Tinh tong cac phan tu vua duong vua chan."""
    tong = 0

    for so in danh_sach:
        if so > 0 and so % 2 == 0:
            tong += so

    return tong


def dem_so_lan_xuat_hien(danh_sach: list[int], k: int) -> int:
    """Dem so lan gia tri k xuat hien trong danh sach."""
    dem = 0

    for so in danh_sach:
        if so == k:
            dem += 1

    return dem


def nhap_danh_sach() -> list[int]:
    """Nhap so nguyen den khi nguoi dung nhap 0."""
    danh_sach = []

    while True:
        try:
            x = int(input("Nhap so nguyen (nhap 0 de ket thuc): "))
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")
            continue

        if x == 0:
            break

        danh_sach.append(x)

    return danh_sach


def main() -> None:
    """Chay chuong trinh cau 3."""
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)

    if any(so > 0 and so % 2 == 0 for so in danh_sach):
        print("Tong cac so duong chan:", tong_so_duong_chan(danh_sach))
    else:
        print("Khong co so duong chan trong danh sach.")

    while True:
        try:
            k = int(input("Nhap gia tri k can dem: "))
            break
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    so_lan = dem_so_lan_xuat_hien(danh_sach, k)

    if so_lan == 0:
        print("Khong co phan tu", k, "trong danh sach.")
    else:
        print("So lan xuat hien cua", k, "la:", so_lan)


if __name__ == "__main__":
    main()
