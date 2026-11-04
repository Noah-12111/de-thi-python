"""Cau 5: Lop DienThoai va cac doi tuong dien thoai."""


class DienThoai:
    """Luu tru va hien thi thong tin mot dien thoai."""

    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int,
    ) -> None:
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self) -> None:
        """Hien thi thong tin cua dien thoai."""
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin)
        print("Gia ban:", self.GiaBan)


def tao_du_lieu_mau() -> list[DienThoai]:
    """Tao hai doi tuong theo du lieu trong de thi."""
    dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    return [dt1, dt2]


def main() -> None:
    """Chay chuong trinh cau 5."""
    danh_sach_dien_thoai = tao_du_lieu_mau()

    for vi_tri, dien_thoai in enumerate(danh_sach_dien_thoai, start=1):
        print("\n=== DIEN THOAI", vi_tri, "===")
        dien_thoai.thongtindienthoai()


if __name__ == "__main__":
    main()
