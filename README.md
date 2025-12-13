
# XÂY DỰNG TRỢ LÝ PHÂN LOẠI CẢM XÚC TIẾNG VIỆT SỬ DỤNG TRANSFORMER (Vietnamese Sentiment Analysis System)


Dự án xây dựng một ứng dụng web đơn giản phục vụ cho việc phân tích cảm xúc (sentiment analysis) trên câu tiếng Việt.



## Tác giả

- Sinh viên thực hiện: Trần Hoàng Khanh 
- MSSVV : 3121410257
- Môn học : Seminar

## Giới thiệu

Dự án xây dựng một ứng dụng web đơn giản phục vụ cho việc phân tích cảm xúc (sentiment analysis) trên câu tiếng Việt. Người dùng chỉ cần nhập một câu bất kỳ, hệ thống sẽ tự động dự đoán cảm xúc của câu thuộc một trong ba lớp: **negative**, **neutral** hoặc **positive**.

Hệ thống còn lưu lại lịch sử các lần phân tích vào dữ liệu cục bộ để tiện cho việc theo dõi và thống kê.

---

## Công nghệ sử dụng

Dự án sử dụng các công nghệ và thư viện chính sau:

* Python 3.x
* Streamlit
* PyTorch
* Transformers / Tokenizer
* Pandas
* NumPy

Mô hình và tokenizer được load thông qua:

```python
from src.model import load_model
```

---

## Cấu trúc thư mục

```
/
│
├── app.py                 # File chạy ứng dụng Streamlit
├── requirements.txt        # Danh sách thư viện cần cài đặt
├── README.md               # File mô tả dự án
│
├── src/
│   ├── model.py            # Load model và tokenizer
│   ├── predict.py          # Hàm dự đoán cảm xúc
│   ├──__init__.py
|
├── history/
    └── sentiment.db          # Lưu lịch sử phân tích

```

---

## Cách cài đặt và chạy chương trình

### Bước 1: Cài đặt thư viện cần thiết 

```bash
pip install -r requirements.txt
```

### Bước 2: Chạy ứng dụng

```bash
streamlit run app.py
```

Sau khi chạy, trình duyệt sẽ mở tại:

```
http://localhost:8501
```

---

## Cách sử dụng

1. Nhập một câu tiếng Việt vào ô văn bản
2. Nhấn nút **Phân tích cảm xúc**
3. Kết quả hiển thị : Nhãn cảm xúc (negative / neutral / positive)
4. Lịch sử của các lần phân tích sẽ hiển thị phía dưới và được lưu trong:

```
history/sentiment.db
```

---

## Hướng phát triển trong tương lai

Dự án có thể mở rộng thêm các chức năng sau:

* Vẽ biểu đồ thống kê tỷ lệ cảm xúc
* Upload file văn bản thay vì chỉ nhập tay
* Hiển thị top-3 cảm xúc thay vì chỉ 1
* Huấn luyện lại với tập dữ liệu lớn hơn
* Đưa ứng dụng lên nền tảng web (Heroku, Streamlit Cloud, v.v.)
