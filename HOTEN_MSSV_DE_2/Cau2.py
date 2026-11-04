"""De 2 - Cau 2: Xu ly chuoi ky tu."""


def DemChuThuong(s):
    dem = 0
    for ky_tu in s:
        if ky_tu.islower():
            dem += 1
    return dem


def DoiXung(s):
    return s == s[::-1]


def main():
    s = input("Nhap chuoi s: ")

    dem = DemChuThuong(s)
    if dem == 0:
        print("Chuoi khong co ky tu chu thuong.")
    else:
        print("So ky tu chu thuong trong chuoi:", dem)

    if DoiXung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Chuoi sau khi viet hoa dau moi tu:", s.title())


if __name__ == "__main__":
    main()
