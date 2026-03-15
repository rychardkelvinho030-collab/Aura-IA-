import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")

# Sua nova chave
API_KEY = "AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws"

# Configuração que força a compatibilidade
genai.configure(api_key=API_KEY)

# Tentativa de inicialização ultra-compatível
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
        # TENTATIVA 1: O modelo mais estável com nome completo
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception:
        try:
            # TENTATIVA 2: Fallback para o modelo Pro caso o Flash falhe no servidor
            model_alt = genai.GenerativeModel('gemini-pro')
            response = model_alt.generate_content(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erro crítico: {e}")
            
