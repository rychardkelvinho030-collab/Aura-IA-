import streamlit as st
import google.generativeai as genai

# Configuração da Interface Aura
st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")
st.caption("Status: Online | Protocolo Jarvis")

# Inserção da Nova Chave
API_KEY = "AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws"

try:
    genai.configure(api_key=API_KEY)
    # Modelo 1.5 Flash: Mais rápido e estável para chaves novas
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de Configuração: {e}")

# Histórico de Memória
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Processamento de Diretivas
if prompt := st.chat_input("Diretiva, Boss..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Gerando a resposta
        response = model.generate_content(f"Você é a Aura IA, assistente pessoal do Boss. Seja eficiente. Diretiva: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Falha no processamento: {e}")
