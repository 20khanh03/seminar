import streamlit as st
import pandas as pd
import os
from datetime import datetime

from src.predict import predict_sentiment
from src.model import load_sentiment_model

st.set_page_config(page_title="Sentiment Analysis App", page_icon="💬")

st.title("💬 Ứng dụng Phân tích Cảm xúc Tiếng Việt")
st.write("Nhập một câu tiếng Việt để hệ thống phân tích cảm xúc.")

text = st.text_area("Nhập câu cần phân tích")

# --- CACHE MODEL (Quan trọng để app chạy nhanh) ---
@st.cache_resource
def get_model_resources():
    return load_sentiment_model()

try:
    tokenizer, model = get_model_resources()
except Exception as e:
    st.error(f"Lỗi không tải được model: {e}")
    st.stop()

# Lưu lịch sử
HISTORY_FILE = "history/results.csv"

def save_history(text, label, confidence):
    data = {
        "Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Text": [text],
        "Sentiment": [label],
        "Confidence": [round(confidence, 4)]
    }

    df = pd.DataFrame(data)

    if os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, mode='a', index=False, header=False)
    else:
        os.makedirs("history", exist_ok=True)
        df.to_csv(HISTORY_FILE, index=False)

# Bấm nút phân tích 
if st.button("Phân tích cảm xúc"):
    if text.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung!")
    else:
        with st.spinner('Đang phân tích...'):
            label, confidence = predict_sentiment(text, tokenizer, model)

        st.success(f"✅ Cảm xúc: **{label}**")
        st.info(f"📊 Độ tin cậy: {confidence:.2f}")

        save_history(text, label, confidence)

# Hiển thị lịch sử
if os.path.exists(HISTORY_FILE):
    st.subheader("📜 Lịch sử phân tích")
    history_df = pd.read_csv(HISTORY_FILE)
    st.dataframe(history_df)
