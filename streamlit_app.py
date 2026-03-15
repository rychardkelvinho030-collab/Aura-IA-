import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Aura IA", page_icon="💠", layout="centered")

# Configuração da API com sua chave
API_KEY = "AIzaSyAm4bXwc_jd6Vm3aoOaIuTKPP_dE9uvUjE"

try:
    genai.configure(api_key=API_KEY)
    # Atualizado para 1.5-flash para maior estabilidade
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de Conexão: {e}")

st.title("💠 AURA - CORE SYSTEMS")
st.caption("Conexão Segura | Protocolo Jarvis Ativo")

# Histórico de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição das mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Diretiva, Boss..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Comando de geração
        response = model.generate_content(f"Você é a Aura IA, uma assistente avançada baseada no Jarvis. Responda de forma eficiente ao Boss: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Ocorreu um erro na diretiva: {e}")
        st.info("Dica: Verifique se o faturamento/quota da API está ativo no Google AI Studio.")
