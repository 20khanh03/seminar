import streamlit as st
import sqlite3
from datetime import datetime
import os
import pandas as pd

from src.predict import predict_sentiment

# ========== GIAO DIỆN ==========
st.set_page_config(page_title="Sentiment Analysis App", page_icon="️🎭")

st.title("Ứng dụng Phân loại Cảm xúc Tiếng Việt")
st.write("Nhập câu tiếng Việt để hệ thống phân tích cảm xúc.")

text = st.text_input("Tối đa 50 ký tự")

DATABASE = "history/sentiment.db"

# ========== TẠO DATABASE ==========
def init_db():
    import os
    os.makedirs("history", exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            sentiment TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()


# ========== LƯU DỮ LIỆU ==========
def save_history(text, sentiment):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (text, sentiment, time)
        VALUES (?, ?, ?)
    """, (text, sentiment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()


# ========== LẤY LỊCH SỬ ==========
def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, text, sentiment, time
        FROM history
        ORDER BY time DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


# Khởi tạo DB khi mở app
init_db()


# ========== NÚT PHÂN LOẠI ==========
if st.button("Phân loại cảm xúc"):

    result, error = predict_sentiment(text)

    if error:
        st.error(error)
    else:
        st.success(f"Kết Quả : {result['sentiment']}")
        save_history(result["text"], result["sentiment"])

# ========== HIỂN THỊ LỊCH SỬ ==========
st.subheader("📜 Lịch Sử Phân Tích")

history = get_history()

# Số dòng hiển thị ban đầu
if "show_limit" not in st.session_state:
    st.session_state.show_limit = 15

if len(history) == 0:
    st.info("Chưa có dữ liệu.")
else:
    # Giới hạn số dòng được hiển thị
    limited_history = history[:st.session_state.show_limit]

    df = pd.DataFrame(
        [ (x[1], x[2], x[3]) for x in limited_history ],
        columns=["Nội dung", "Cảm xúc", "Thời gian"]
    )

    # ĐỔI TEXT CẢM XÚC ĐỂ HIỂN THỊ
    df["Cảm xúc"] = df["Cảm xúc"].str.lower().map({
        "positive - tích cực": "Tích cực",
        "positive": "Tích cực",
        "negative - tiêu cực": "Tiêu cực",
        "negative": "Tiêu cực",
        "neutral - trung tính": "Trung tính",
        "neutral": "Trung tính",
    }).fillna("Khác")

    def color_sentiment(val):
        if val == "Tích cực":
            return "color: green; font-weight: bold"
        elif val == "Tiêu cực":
            return "color: red; font-weight: bold"
        else:
            return "color: blue; font-weight: bold"

    styled_df = df.style.applymap(color_sentiment, subset=["Cảm xúc"])

    # Hiển thị bảng
    st.dataframe(
        styled_df,
        use_container_width=True,
        height=400
    )

    # NÚT TẢI THÊM
    if st.session_state.show_limit < len(history):
        if st.button("🔽 Tải thêm"):
            st.session_state.show_limit += 15
            st.rerun()
    else:
        st.success("✅ Đã hiển thị tất cả dữ liệu")
