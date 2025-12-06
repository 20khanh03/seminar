from src.model import load_model

shortcode_dict = {
    "ko": "không",
    "k": "không",
    "hok": "không",
    "dc": "được",
    "đc": "được",
    "tks": "cảm ơn",
    "thanks": "cảm ơn",
    "good": "tốt",
    "bad": "tệ",
    "ok": "tốt",
    "vs": "với",
    "ntn": "như thế nào",
    "wa": "quá",
    "qá": "quá"
}

def correct_shortcode(text):
    text_lower = text.lower()
    words = text_lower.split()
    corrected_words = []
    
    for word in words:
        if word in shortcode_dict:
            corrected_words.append(shortcode_dict[word])
        else:
            corrected_words.append(word)
            
    return " ".join(corrected_words)

def predict_sentiment(text):
    raw_input = text.strip()

    # Chuyển từ "k, ko, dc" sang "không, được" TRƯỚC khi đưa vào model
    clean_text = correct_shortcode(raw_input)

    if len(clean_text) < 3:
        return None, "Câu quá ngắn, vui lòng nhập lại."

    if len(clean_text) > 50:
        return None, f"Câu quá dài ({len(clean_text)}/50 ký tự). Yêu cầu tối đa 50 ký tự."

    pipeline = load_model()

    try:
        result = pipeline(clean_text)[0] 
        score = result["score"]
        raw_label = result["label"] # Model này trả về: POS, NEG, hoặc NEU
        
        if raw_label == "NEG":
            final_label = "NEGATIVE - TIÊU CỰC"
        elif raw_label == "POS":
            final_label = "POSITIVE - TÍCH CỰC"
        elif raw_label == "NEU":
            final_label = "NEUTRAL - TRUNG TÍNH"
        else:
            final_label = "NEUTRAL - TRUNG TÍNH"
        
        if score < 0.5: 
            final_label = "NEUTRAL - TRUNG TÍNH"

        output = {
            "text": raw_input,             # Text gốc user nhập (để hiển thị lại cho user)
            "processed_text": clean_text,  # Text đã chỉnh shortcode (để bạn debug xem nó sửa đúng ko)
            "sentiment": final_label,
            "score": round(score, 4)
        }
        return output, None

    except Exception as e:
        return None, f"Lỗi xử lý AI: {str(e)}"