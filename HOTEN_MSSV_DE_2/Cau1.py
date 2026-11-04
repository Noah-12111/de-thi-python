"""De 2 - Cau 1: Tong cac uoc so va tinh S."""


def TongUocSo(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong


def S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i ** i
    return tong


def main():
    n = int(input("Nhap n (1 <= n <= 99): "))
    while n < 1 or n > 99:
        n = int(input("Nhap lai n (1 <= n <= 99): "))

    print("Tong cac uoc so la:", TongUocSo(n))
    print("S =", S(n))


if __name__ == "__main__":
    main()
