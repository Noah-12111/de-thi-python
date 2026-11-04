# Bộ lời giải đề thi kết thúc môn Lập trình Python

Repository lưu lời giải cho **mã đề 11301** của môn **Lập trình Python (mã môn 229152)**, theo đề và đáp án mẫu trong PDF được cung cấp.

Mục tiêu của bộ bài làm là bám sát yêu cầu đề thi, sử dụng cú pháp Python cơ bản, đặt tên biến dễ hiểu và có chú thích để thuận tiện ôn tập.

## 1. Cấu trúc thư mục

```text
de-thi-python/
├── README.md
└── HOTEN_MSSV/
    ├── Cau1.py
    ├── Cau2.py
    ├── Cau3.py
    ├── Cau4.py
    └── Cau5.py
```

**Lưu ý khi nộp bài:** đề yêu cầu một thư mục theo mẫu `HOTEN_MSSV` chứa đúng 5 file `.py`. Trước khi nộp, hãy đổi tên thư mục này theo họ tên và mã số sinh viên của bạn theo đúng quy định của giảng viên. Không cần đổi tên 5 file bài làm.

## 2. Yêu cầu chạy chương trình

- Python 3.8 trở lên.
- Không cần cài thư viện ngoài bằng `pip`.
- Có thể chạy bằng VS Code, PyCharm hoặc Terminal.

Ví dụ chạy câu 1:

```bash
python HOTEN_MSSV/Cau1.py
```

Trên Windows cũng có thể dùng lệnh:

```powershell
py .\HOTEN_MSSV\Cau1.py
```

Thay `Cau1.py` bằng `Cau2.py`, `Cau3.py`, `Cau4.py` hoặc `Cau5.py` để chạy câu tương ứng. Mỗi file là một chương trình độc lập.

## 3. Nội dung từng câu

### Câu 1 - Số nguyên và hàm

File: `HOTEN_MSSV/Cau1.py`

1. Nhập số nguyên dương `n`; nếu `n` nằm ngoài đoạn từ 1 đến 1500 thì yêu cầu nhập lại.
2. Hàm `DemChuSoLe(n)` dùng phép chia lấy dư `%` để tách từng chữ số, sau đó đếm chữ số lẻ.
3. Hàm `S(n)` tính tổng:

   `S = 1/2 + 1/4 + 1/6 + ... + 1/(2*n)`

**Ví dụ:** nhập `n = 635`, chương trình đếm được 2 chữ số lẻ (3 và 5).

**Kiến thức cần nhớ:** `while`, `for`, phép chia lấy dư `%`, phép chia nguyên `//`, hàm và giá trị trả về `return`.

### Câu 2 - Xử lý chuỗi

File: `HOTEN_MSSV/Cau2.py`

1. Hàm `DemChuHoa(s)` duyệt chuỗi và dùng `isupper()` để đếm ký tự viết hoa.
2. Hàm `DoiXung(s)` so sánh chuỗi ban đầu với chuỗi đảo ngược `s[::-1]`.
3. Hàm `TongChuSo(s)` dùng `isdigit()` để nhận diện chữ số và cộng các chữ số đó.

**Ví dụ:** nhập `AbcA21` thì có 2 ký tự viết hoa, chuỗi không đối xứng và tổng chữ số bằng 3.

**Lưu ý:** kiểm tra đối xứng được thực hiện đúng theo cách so sánh toàn bộ chuỗi trong đáp án mẫu; chữ hoa/chữ thường, khoảng trắng và ký tự đặc biệt đều được giữ nguyên khi so sánh.

**Kiến thức cần nhớ:** duyệt chuỗi bằng `for`, `isupper()`, `isdigit()`, ép kiểu `int()` và cắt chuỗi đảo ngược `[::-1]`.

### Câu 3 - Danh sách

File: `HOTEN_MSSV/Cau3.py`

1. Tạo danh sách rỗng `danh_sach = []`.
2. Nhập số nguyên liên tục; nhập `0` để kết thúc. Số 0 chỉ là ký hiệu dừng, không được thêm vào danh sách.
3. Duyệt danh sách để tính tổng các số dương chẵn.
4. Nhập `k` và đếm số lần `k` xuất hiện trong danh sách.

Chương trình có xử lý trường hợp người dùng nhập dữ liệu không phải số nguyên ở bước nhập danh sách.

**Kiến thức cần nhớ:** list, `append()`, vòng lặp `while`, `break`, điều kiện kết hợp `and` và biến đếm.

### Câu 4 - Từ điển quản lý sách

File: `HOTEN_MSSV/Cau4.py`

1. Nhập số lượng sách `n > 0`.
2. Với mỗi sách, nhập mã số, tên sách, tên tác giả, nhà xuất bản và năm xuất bản.
3. Lưu thông tin trong từ điển `tu_dien`, trong đó mã số sách là **key**; giá trị là danh sách gồm tên sách, tác giả, nhà xuất bản và năm xuất bản.
4. Không chấp nhận năm xuất bản lớn hơn năm hiện tại.
5. Nhập mã số cần xóa. Nếu mã tồn tại thì dùng `del` để xóa; nếu không thì thông báo không tìm thấy.

**Ví dụ cấu trúc dữ liệu:**

```python
{
    "S001": ["Python Co Ban", "Nguyen Van A", "NXB Tre", 2020]
}
```

**Kiến thức cần nhớ:** dictionary, key/value, `datetime.now().year`, toán tử `in`, `del` và danh sách dùng làm giá trị.

### Câu 5 - Lập trình hướng đối tượng

File: `HOTEN_MSSV/Cau5.py`

Tạo lớp `DienThoai` với 5 thuộc tính:

- `MaMay`
- `TenMay`
- `HangSanXuat`
- `DungLuongPin`
- `GiaBan`

Lớp có phương thức khởi tạo `__init__()` để gán dữ liệu cho thuộc tính và phương thức `thongtindienthoai()` để hiển thị thông tin.

Chương trình tạo đúng hai đối tượng theo đề:

| Mã máy | Tên máy | Hãng | Dung lượng pin | Giá bán |
|---|---|---|---:|---:|
| DT01 | iPhone 15 Pro | Apple | 3274 | 28.990.000 |
| DT02 | Galaxy S24 Ultra | Samsung | 5000 | 29.990.000 |

**Kiến thức cần nhớ:** class, object, `self`, `__init__()`, thuộc tính và phương thức.

## 4. Cách ôn tập nhanh

| Câu | Nội dung trọng tâm | Từ khóa nên nhớ |
|---|---|---|
| 1 | Xử lý chữ số và tính tổng | `%`, `//`, `while`, `for`, `return` |
| 2 | Xử lý chuỗi | `isupper()`, `isdigit()`, `[::-1]` |
| 3 | Danh sách | `[]`, `append()`, `break`, `for` |
| 4 | Từ điển | `{}`, key, value, `in`, `del` |
| 5 | Lớp và đối tượng | `class`, `self`, `__init__()` |

## 5. Ghi chú

- Các lời giải được tách thành 5 file độc lập theo cấu trúc bài thi.
- Tên hàm, lớp và các trường dữ liệu được giữ gần với đề/đáp án để dễ đối chiếu.
- Kết quả tính tổng ở câu 1 là số thực Python; có thể xuất hiện nhiều chữ số sau dấu thập phân do cách biểu diễn số thực.
- Đây là bài làm thực hành cơ bản, ưu tiên cách viết rõ ràng và dễ học thuộc; không sử dụng framework hay thư viện bên ngoài.
