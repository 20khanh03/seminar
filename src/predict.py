# src/predict.py
from src.model import load_model

def predict_sentiment(text):
    # 1. Kiểm tra độ dài (Yêu cầu thầy)
    clean_text = text.strip()
    if len(clean_text) < 3:
        return None, "Câu quá ngắn, vui lòng nhập lại."

    if len(clean_text) > 50:
        return None, f"Câu quá dài ({len(clean_text)}/50 ký tự). Yêu cầu tối đa 50 ký tự."

    # 2. Load model (lấy từ cache)
    pipeline = load_model()

    # 3. Dự đoán
    try:
        result = pipeline(clean_text)[0]
        score = result["score"]
        raw_label = result["label"] # Model này trả về: POS, NEG, hoặc NEU
        
        # Mapping sang Tiếng Việt/Tiếng Anh chuẩn để hiển thị
        if raw_label == "NEG":
            final_label = "NEGATIVE - TIÊU CỰC"
        elif raw_label == "POS":
            final_label = "POSITIVE - TÍCH CỰC"
        elif raw_label == "NEU":
            final_label = "NEUTRAL - TRUNG TÍNH"
        else:
            final_label = "NEUTRAL - TRUNG TÍNH"
        
        # Logic phụ: Nếu model không chắc chắn lắm (score thấp), gán về Neutral
        # (Tùy chọn, nhưng giữ lại cho an toàn)
        if score < 0.5: 
            final_label = "NEUTRAL - TRUNG TÍNH"

        output = {
            "text": clean_text,
            "sentiment": final_label,
            "score": round(score, 4)
        }
        return output, None

    except Exception as e:
        return None, f"Lỗi xử lý AI: {str(e)}"