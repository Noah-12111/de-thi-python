"""Cau 2 - Dem chu hoa, kiem tra doi xung va tinh tong chu so."""


def DemChuHoa(s):
    """Dem cac ky tu chu hoa trong chuoi s."""
    dem = 0
    for ky_tu in s:
        if ky_tu.isupper():
            dem += 1
    return dem


def DoiXung(s):
    """Tra ve True neu chuoi s doi xung."""
    return s == s[::-1]


def TongChuSo(s):
    """Tinh tong cac ky tu la chu so trong chuoi s."""
    tong = 0
    for ky_tu in s:
        if ky_tu.isdigit():
            tong += int(ky_tu)
    return tong


def main():
    s = input("Nhap chuoi s: ")

    dem = DemChuHoa(s)
    if dem == 0:
        print("Chuoi khong co ky tu chu hoa.")
    else:
        print("So ky tu chu hoa:", dem)

    if DoiXung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Tong cac chu so trong chuoi:", TongChuSo(s))


if __name__ == "__main__":
    main()
