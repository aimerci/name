# 簡単なStreamlit GUIの例
import streamlit as st

st.title("こんにちは！")
text = st.text_input("名前を入力してください")
if st.button("挨拶する"):
    st.write(f"{text}さん、こんにちは！")
