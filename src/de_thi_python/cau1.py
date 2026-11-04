"""Cau 1: Kiem tra so nguyen, dem chu so le va tinh tong S."""


def dem_chu_so_le(n: int) -> int:
    """Tra ve so luong chu so le cua so nguyen duong n."""
    if n < 0:
        raise ValueError("n phai la so nguyen khong am.")

    dem = 0

    while n != 0:
        chu_so = n % 10

        if chu_so % 2 != 0:
            dem += 1

        n //= 10

    return dem


def tinh_s(n: int) -> float:
    """Tinh S = 1/2 + 1/4 + 1/6 + ... + 1/(2*n)."""
    if n < 1:
        raise ValueError("n phai lon hon hoac bang 1.")

    tong = 0.0

    for i in range(1, n + 1):
        tong += 1 / (2 * i)

    return tong


def nhap_n() -> int:
    """Nhap n va kiem tra n thuoc doan [1, 1500]."""
    while True:
        try:
            n = int(input("Nhap n (1 <= n <= 1500): "))
            if 1 <= n <= 1500:
                return n
            print("n khong hop le. Vui long nhap lai.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")


def main() -> None:
    """Chay chuong trinh cau 1."""
    n = nhap_n()

    print("So luong chu so le:", dem_chu_so_le(n))
    print("S =", tinh_s(n))


if __name__ == "__main__":
    main()
