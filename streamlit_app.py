import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Aura IA", page_icon="💠")

# Use sua chave API aqui
genai.configure(api_key="SUA_API_KEY_AQUI")
model = genai.GenerativeModel('gemini-pro')

st.title("💠 AURA - SISTEMA ONLINE")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Diretiva, Boss..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = model.generate_content(f"Você é a Aura IA. Responda ao Boss: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
