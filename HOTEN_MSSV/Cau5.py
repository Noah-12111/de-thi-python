"""Cau 5 - Tao lop DienThoai va hien thi thong tin doi tuong."""


class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin)
        print("Gia ban:", self.GiaBan)


def main():
    # Tao hai doi tuong theo dung du lieu trong de thi.
    DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print("=== THONG TIN DIEN THOAI 1 ===")
    DT1.thongtindienthoai()

    print("\n=== THONG TIN DIEN THOAI 2 ===")
    DT2.thongtindienthoai()


if __name__ == "__main__":
    main()
