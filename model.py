from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    model_name = "wonrax/phobert-base-vietnamese-sentiment"

    sentiment_pipeline = pipeline(
        task="sentiment-analysis",
        model=model_name,
        tokenizer=model_name
    )
    
    return sentiment_pipeline