"""Cau 3 - Nhap va xu ly danh sach so nguyen."""


def main():
    danh_sach = []

    # Nhap cac so nguyen; nhap 0 de ket thuc.
    while True:
        try:
            x = int(input("Nhap so nguyen (nhap 0 de dung): "))
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap mot so nguyen!")
            continue

        if x == 0:
            break

        danh_sach.append(x)

    print("Danh sach vua nhap:", danh_sach)

    # Tinh tong cac so duong chan.
    tong = 0
    dem_so_duong_chan = 0
    for x in danh_sach:
        if x > 0 and x % 2 == 0:
            tong += x
            dem_so_duong_chan += 1

    if dem_so_duong_chan == 0:
        print("Khong co so duong chan trong danh sach.")
    else:
        print("Tong cac so duong chan trong danh sach:", tong)

    # Dem so lan xuat hien cua k.
    k = int(input("Nhap gia tri k can dem: "))
    dem = 0
    for x in danh_sach:
        if x == k:
            dem += 1

    if dem == 0:
        print("Khong co phan tu", k, "trong danh sach.")
    else:
        print("So lan xuat hien cua", k, "la:", dem)


if __name__ == "__main__":
    main()
