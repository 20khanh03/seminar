# Vietnamese Sentiment Analysis System (Streamlit Application)

## 1. Giới thiệu

Dự án xây dựng một ứng dụng web đơn giản phục vụ cho việc phân tích cảm xúc (sentiment analysis) trên câu tiếng Việt. Người dùng chỉ cần nhập một câu bất kỳ, hệ thống sẽ tự động dự đoán cảm xúc của câu thuộc một trong ba lớp: **negative**, **neutral** hoặc **positive**.

Ứng dụng được phát triển bằng **Streamlit** cho giao diện và sử dụng mô hình học sâu (deep learning) đã được huấn luyện sẵn để thực hiện việc phân loại cảm xúc.

Bên cạnh việc hiển thị kết quả, hệ thống còn lưu lại lịch sử các lần phân tích vào file CSV để tiện cho việc theo dõi và thống kê.

---

## 2. Công nghệ sử dụng

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

## 3. Cấu trúc thư mục

```
seminar/
│
├── app.py                 # File chạy ứng dụng Streamlit
├── requirements.txt        # Danh sách thư viện cần cài đặt
├── README.md               # File mô tả dự án
│
├── src/
│   ├── model.py            # Load model và tokenizer
│   ├── predict.py          # Hàm dự đoán cảm xúc
│
├── history/
│   └── results.csv          # Lưu lịch sử phân tích
│
└── venv/                    # Môi trường ảo (không push lên GitHub)
```

---

## 4. Cách cài đặt và chạy chương trình

### Bước 1: Tạo môi trường ảo

```bash
python -m venv venv
venv\Scripts\activate     (Windows)
```

### Bước 2: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Bước 3: Chạy ứng dụng

```bash
streamlit run app.py
```

Sau khi chạy, trình duyệt sẽ mở tại:

```
http://localhost:8501
```

---

## 5. Cách sử dụng

1. Nhập một câu tiếng Việt vào ô văn bản
2. Nhấn nút **Phân tích cảm xúc**
3. Kết quả hiển thị gồm:

   * Nhãn cảm xúc (negative / neutral / positive)
   * Độ tin cậy (confidence score)
4. Lịch sử của các lần phân tích sẽ hiển thị phía dưới và được lưu trong:

```
history/results.csv
```

---

## 6. Ý nghĩa của độ tin cậy (Confidence)

Độ tin cậy được tính bằng xác suất lớn nhất sau khi áp dụng hàm **Softmax** lên đầu ra của mô hình.

Trong quá trình thử nghiệm, nhiều dự đoán cho kết quả dưới 0.5, điều này có thể xuất phát từ một số nguyên nhân:

* Dữ liệu huấn luyện chưa đủ lớn hoặc chưa đa dạng
* Mô hình chưa được fine-tune tối ưu cho tiếng Việt
* Câu đầu vào có nội dung trung tính hoặc không rõ cảm xúc
* Câu quá ngắn hoặc mơ hồ về ngữ nghĩa

Tuy nhiên, hệ thống vẫn cho ra nhãn hợp lý và có thể cải thiện thêm bằng việc:

* Mở rộng tập dữ liệu
* Fine-tune thêm model
* Cân bằng lại dữ liệu giữa các lớp

---

## 7. Hướng phát triển trong tương lai

Dự án có thể mở rộng thêm các chức năng sau:

* Vẽ biểu đồ thống kê tỷ lệ cảm xúc
* Upload file văn bản thay vì chỉ nhập tay
* Hiển thị top-3 cảm xúc thay vì chỉ 1
* Huấn luyện lại với tập dữ liệu lớn hơn
* Đưa ứng dụng lên nền tảng web (Heroku, Streamlit Cloud, v.v.)

---

## 8. Tác giả

Sinh viên thực hiện: [Bổ sung họ tên tại đây]
Môn học / Seminar: [Bổ sung tại đây]
Ngày thực hiện: [Bổ sung tại đây]
