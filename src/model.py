import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Đổi tên model thành đường dẫn thư mục
MODEL_PATH = "./model_files" 

def load_sentiment_model():
    print(f"Đang tải model từ {MODEL_PATH}...")
    
    # Kiểm tra xem thư mục có tồn tại không để tránh crash
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Không tìm thấy thư mục model tại {MODEL_PATH}. Hãy chạy script tải model trước!")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    
    return tokenizer, model