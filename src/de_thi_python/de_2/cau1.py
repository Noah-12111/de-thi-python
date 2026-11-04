"""De 2 - Cau 1: Tong uoc so va tinh S = 1 + 2^2 + ... + n^n."""


def tong_uoc_so(n: int) -> int:
    """Tinh tong cac uoc so duong cua n."""
    if n < 1:
        raise ValueError("n phai la so nguyen duong.")

    tong = 0

    for i in range(1, n + 1):
        if n % i == 0:
            tong += i

    return tong


def tinh_s(n: int) -> int:
    """Tinh S = 1 + 2^2 + 3^3 + ... + n^n."""
    if n < 1:
        raise ValueError("n phai lon hon hoac bang 1.")

    tong = 0

    for i in range(1, n + 1):
        tong += i ** i

    return tong


def nhap_n() -> int:
    """Nhap n trong doan tu 1 den 99."""
    while True:
        try:
            n = int(input("Nhap n (1 <= n <= 99): "))
            if 1 <= n <= 99:
                return n
            print("Gia tri khong hop le. Vui long nhap lai.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")


def main() -> None:
    """Chay chuong trinh De 2 - Cau 1."""
    n = nhap_n()
    print("Tong cac uoc so cua", n, "la:", tong_uoc_so(n))
    print("S =", tinh_s(n))


if __name__ == "__main__":
    main()
