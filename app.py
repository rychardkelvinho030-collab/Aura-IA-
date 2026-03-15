import streamlit as st
import google.generativeai as genai

# Configuração simples e direta
st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")

# Conectando ao cérebro
genai.configure(api_key="AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws")
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Diretiva, Boss..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Chamada da IA
        response = model.generate_content(f"Você é a Aura, uma IA sofisticada. Responda ao Boss: {prompt}")
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erro: {e}")
