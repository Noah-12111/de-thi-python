"""Cau 1 - Kiem tra so nguyen va viet ham xu ly so."""


def DemChuSoLe(n):
    """Dem so chu so le trong so nguyen duong n."""
    dem = 0

    while n != 0:
        chu_so = n % 10
        if chu_so % 2 != 0:
            dem += 1
        n //= 10

    return dem


def S(n):
    """Tinh S = 1/2 + 1/4 + ... + 1/(2*n)."""
    tong = 0

    for i in range(1, n + 1):
        tong += 1 / (2 * i)

    return tong


def main():
    # Nhap lai neu n khong nam trong doan tu 1 den 1500.
    n = int(input("Nhap so nguyen duong n (1 <= n <= 1500): "))
    while n < 1 or n > 1500:
        print("Gia tri khong hop le. Vui long nhap lai!")
        n = int(input("Nhap n (1 <= n <= 1500): "))

    print("So luong chu so le la:", DemChuSoLe(n))
    print("Gia tri S =", S(n))


if __name__ == "__main__":
    main()
