import streamlit as st
import sys
import os

# Garante que o Python encontre o módulo 'core'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.llm_engine import CipherEngine

# --- Configuração da Página ---
st.set_page_config(
    page_title="CIPHER IA - Cybersecurity Expert",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estética Cyberdeck (CSS customizado)
st.markdown("""
    <style>
    .stChatMessage {
        background-color: #0e1117;
        border: 1px solid #1f2937;
        border-radius: 8px;
        padding: 10px;
    }
    .stChatInput {
        border: 1px solid #00ff00;
    }
    .cyber-header {
        text-align: center;
        color: #00ff00;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

# --- Inicialização do Motor (Modo Web = Nuvem via Groq) ---
@st.cache_resource
def load_engine():
    try:
        return CipherEngine(mode='web')
    except Exception as e:
        st.error(f"❌ Erro ao conectar com a Nuvem: {e}")
        st.info("Verifique se a GROQ_API_KEY está no seu arquivo .env")
        st.stop()

engine = load_engine()

# Carregar System Prompt
base_dir = os.path.dirname(os.path.abspath(__file__))
prompt_path = os.path.join(base_dir, "prompts", "system_prompt.txt")
try:
    with open(prompt_path, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
except FileNotFoundError:
    st.error("❌ system_prompt.txt não encontrado em prompts/")
    st.stop()

# --- Interface Principal ---
st.markdown('<div class="cyber-header">', unsafe_allow_html=True)
st.title("🛡️ CIPHER IA")
st.subheader("Cybersecurity Expert | Red Team + Blue Team")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("Conectado via Groq API (120B Parâmetros) • Arquitetura Híbrida • Padrão CVSS")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controles")
    if st.button("🧹 Limpar Memória (Chat)"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.info("""
    💡 **Modos de Operação:**
    
    🔧 **Diagnóstico:** Peça verificações de sistema (ex: 'verifique portas abertas')
    
    🛡️ **Análise:** Descreva cenários para análise de vulnerabilidade
    
    💬 **Consulta:** Pergunte sobre conceitos de segurança
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Exemplos Rápidos")
    st.markdown("- 'Analise a segurança do SSH padrão'")
    st.markdown("- 'O que é MITRE ATT&CK?'")
    st.markdown("- 'Verifique processos suspeitos'")

# --- Gerenciamento de Estado (Histórico) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Se for um comando EXECUTE:, mostra como bloco de código
        if message["role"] == "assistant" and message["content"].startswith("EXECUTE:"):
            cmd = message["content"].replace("EXECUTE:", "").strip()
            st.code(cmd, language="bash")
            st.caption("☝️ Copie e execute este comando no seu terminal Linux")
        else:
            st.markdown(message["content"])

# --- Loop de Interação ---
if prompt := st.chat_input("Operador, qual a sua ordem?"):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("🛡️ Analisando através de lentes de segurança..."):
            try:
                resposta = engine.generate(prompt, system_prompt, st.session_state.messages[:-1])
                
                # Renderiza a resposta
                if resposta.startswith("EXECUTE:"):
                    cmd = resposta.replace("EXECUTE:", "").strip()
                    st.code(cmd, language="bash")
                    st.caption("☝️ Copie e execute este comando no seu terminal Linux")
                else:
                    st.markdown(resposta)
                
                # Salva no histórico
                st.session_state.messages.append({"role": "assistant", "content": resposta})
                
            except Exception as e:
                st.error(f"❌ Erro na inferência: {e}")
