"""De 2 - Cau 3: Nhap va xu ly danh sach so nguyen."""


def main():
    danh_sach = []

    while True:
        x = int(input("Nhap danh sach (nhap 0 de dung): "))
        if x == 0:
            break
        danh_sach.append(x)

    print("Danh sach vua nhap:", danh_sach)

    duong_chan = []
    for x in danh_sach:
        if x > 0 and x % 2 == 0:
            duong_chan.append(x)

    if duong_chan:
        print("Cac so duong chan co trong danh sach:", duong_chan)
    else:
        print("Khong co so duong chan trong danh sach.")

    k = int(input("Nhap k: "))
    dem = danh_sach.count(k)

    if dem == 0:
        print(k, "khong co trong danh sach.")
    else:
        print(k, "xuat hien", dem, "lan.")


if __name__ == "__main__":
    main()
