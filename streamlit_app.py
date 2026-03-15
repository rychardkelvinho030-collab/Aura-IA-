import streamlit as st
import google.generativeai as genai

# Configuração da Interface
st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")

# Chave API Direta
API_KEY = "AIzaSyAm4bXwc_jd6Vm3aoOaIuTKPP_dE9uvUjE"

# Inicialização do Modelo
@st.cache_resource
def load_model():
    genai.configure(api_key=API_KEY)
    # Usando o nome completo do modelo para evitar o erro 404
    return genai.GenerativeModel('models/gemini-1.5-flash')

model = load_model()

# Histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Processamento
if prompt := st.chat_input("Diretiva, Boss..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Gerar resposta com tratamento de erro
        response = model.generate_content(prompt)
        
        if response.text:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Sistema offline: {e}")
        st.info("Boss, se o erro 404 continuar, pode ser que esta API Key específica tenha expirado ou precise de uma nova geração no Google AI Studio.")
