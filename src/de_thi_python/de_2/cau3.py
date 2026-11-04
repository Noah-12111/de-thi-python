"""De 2 - Cau 3: Nhap va xu ly danh sach so nguyen."""


def lay_so_duong_chan(danh_sach: list[int]) -> list[int]:
    """Tra ve danh sach gom cac so duong chan."""
    ket_qua = []

    for so in danh_sach:
        if so > 0 and so % 2 == 0:
            ket_qua.append(so)

    return ket_qua


def dem_so_lan_xuat_hien(danh_sach: list[int], k: int) -> int:
    """Dem so lan phan tu k xuat hien trong danh sach."""
    return danh_sach.count(k)


def nhap_danh_sach() -> list[int]:
    """Nhap so nguyen den khi nguoi dung nhap 0."""
    danh_sach = []

    while True:
        try:
            x = int(input("Nhap so nguyen (nhap 0 de ket thuc): "))
        except ValueError:
            print("Vui long nhap mot so nguyen.")
            continue

        if x == 0:
            break

        danh_sach.append(x)

    return danh_sach


def main() -> None:
    """Chay chuong trinh De 2 - Cau 3."""
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)

    so_duong_chan = lay_so_duong_chan(danh_sach)
    if so_duong_chan:
        print("Cac so duong chan co trong danh sach:", so_duong_chan)
    else:
        print("Khong co so duong chan trong danh sach.")

    while True:
        try:
            k = int(input("Nhap k: "))
            break
        except ValueError:
            print("Vui long nhap k la so nguyen.")

    dem = dem_so_lan_xuat_hien(danh_sach, k)
    if dem == 0:
        print(k, "khong co trong danh sach.")
    else:
        print(k, "xuat hien", dem, "lan.")


if __name__ == "__main__":
    main()
