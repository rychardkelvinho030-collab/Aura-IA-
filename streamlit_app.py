import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aura IA", page_icon="💠")
st.title("💠 AURA - CORE SYSTEMS")

# Sua nova chave de energia
API_KEY = "AIzaSyDVZ_MB9WchWO0yL_fWvi421eemvS9FQws"

# Configuração de Reconhecimento Direto
genai.configure(api_key=API_KEY)

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
        # TÉCNICA ALPHA: Forçando o caminho absoluto do modelo
        # Isso contorna o erro 404 da v1beta
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        
        # Gerando resposta
        response = model.generate_content(prompt)
        
        if response:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        # SE O FLASH FALHAR, TENTA O PRO IMEDIATAMENTE
        try:
            model_pro = genai.GenerativeModel(model_name="models/gemini-pro")
            response = model_pro.generate_content(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e_final:
            st.error(f"Erro de Conexão: {e_final}")
            st.info("Boss, se o erro 404 continuar aqui, o servidor do Streamlit precisa ser reiniciado manualmente.")
