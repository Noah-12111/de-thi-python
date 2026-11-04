"""De 2 - Cau 5: Lop MonHoc va cac doi tuong mon hoc."""


class MonHoc:
    """Luu tru va hien thi thong tin mot mon hoc."""

    def __init__(
        self,
        MaMonHoc: int,
        TenMonHoc: str,
        SoTinChi: int,
        KhoaPhuTrach: str,
    ) -> None:
        self.MaMonHoc = MaMonHoc
        self.TenMonHoc = TenMonHoc
        self.SoTinChi = SoTinChi
        self.KhoaPhuTrach = KhoaPhuTrach

    def thongtinmonhoc(self) -> None:
        """Hien thi thong tin cua mon hoc."""
        print("Ma mon hoc:", self.MaMonHoc)
        print("Ten mon hoc:", self.TenMonHoc)
        print("So tin chi:", self.SoTinChi)
        print("Khoa phu trach:", self.KhoaPhuTrach)


def tao_du_lieu_mau() -> list[MonHoc]:
    """Tao hai doi tuong theo dung du lieu trong de thi."""
    csdl = MonHoc(229008, "Co so du lieu", 3, "Cong nghe thong tin")
    tieng_anh = MonHoc(224604, "Tieng Anh 1", 2, "Ngoai ngu")

    return [csdl, tieng_anh]


def main() -> None:
    """Chay chuong trinh De 2 - Cau 5."""
    danh_sach_mon_hoc = tao_du_lieu_mau()

    for vi_tri, mon_hoc in enumerate(danh_sach_mon_hoc, start=1):
        print("\n=== MON HOC", vi_tri, "===")
        mon_hoc.thongtinmonhoc()


if __name__ == "__main__":
    main()
