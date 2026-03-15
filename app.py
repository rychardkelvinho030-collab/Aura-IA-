import streamlit as st
import google.generativeai as genai

# Protocolo Aura
st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")

# Chave de Energia
API_KEY = "AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws"

# Configuração com o modelo correto (1.5-flash)
genai.configure(api_key=API_KEY)
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
        # Prompt de Sistema para Personalidade
        contexto = "Você é a Aura, uma inteligência artificial sofisticada baseada no sistema Jarvis. Responda de forma prestativa, inteligente e chame o usuário de Boss."
        response = model.generate_content(f"{contexto}\n\nBoss disse: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erro nos Sistemas: {e}")
