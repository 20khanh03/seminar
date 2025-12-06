# src/predict.py
import torch

def predict_sentiment(text, tokenizer, model):
    # 1. Xử lý text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    
    # 2. Đưa vào model
    with torch.no_grad():
        outputs = model(**inputs)
    
    # 3. Tính toán xác suất
    probs = torch.softmax(outputs.logits, dim=1)
    label_idx = torch.argmax(probs).item()
    score = probs[0][label_idx].item()
    
    # Mapping nhãn (Cần check lại model wonrax cụ thể trả về gì)
    # Ví dụ: 0: NEG, 1: POS, 2: NEU
    labels_map = {0: "Tiêu cực", 1: "Tích cực", 2: "Trung tính"} 
    
    return labels_map.get(label_idx, "Không rõ"), score