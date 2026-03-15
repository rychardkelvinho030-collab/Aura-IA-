import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="Aura IA", page_icon="💠", layout="centered")

# CSS para deixar com cara de sistema Jarvis
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stChatMessage { border-radius: 15px; border: 1px solid #1f2937; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💠 AURA - CORE SYSTEMS")
st.caption("Status: Operacional | Protocolo Jarvis v3.0")

# --- NÚCLEO DE ENERGIA (API) ---
API_KEY = "AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws"

# Configuração forçando o transporte via REST para evitar erros de versão
genai.configure(api_key=API_KEY, transport='rest')

# Usando o nome do modelo sem o prefixo 'models/' para testar a rota direta
model = genai.GenerativeModel('gemini-1.5-flash')
---"
# Configuração do Motor com endereçamento direto
genai.configure(api_key=API_KEY)
# Usando o caminho completo para evitar erro de versão da API
model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

# --- MEMÓRIA DO SISTEMA ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição do Histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- PROCESSAMENTO DE DIRETIVAS ---
if prompt := st.chat_input("Diretiva, Boss..."):
    # Mostra a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Prompt de Personalidade embutido no sistema
        contexto = (
            "Você é a Aura, uma inteligência artificial de elite, sofisticada e eficiente, "
            "baseada no protocolo Jarvis. Você é prestativa, usa termos técnicos ocasionalmente "
            "e deve SEMPRE chamar o usuário de Boss. Responda de forma clara e direta."
        )
        
        # Gerando a resposta com o modelo flash (mais rápido)
        full_prompt = f"{contexto}\n\nBoss disse: {prompt}"
        response = model.generate_content(full_prompt)
        
        # Exibe a resposta da Aura
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"Falha Crítica nos Sistemas: {e}")
        st.info("Dica: Se o erro for 404, verifique se o 'Manual Deploy -> Clear build cache' foi executado no Render.")
