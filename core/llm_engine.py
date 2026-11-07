import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class CipherEngine:
    """
    Motor de Inferência Híbrido do CIPHER IA v2.
    CLI: Usa Ollama Local (Qwen2.5 3B)
    WEB: Usa Groq API (Modelo 120B)
    """
    
    def __init__(self, mode='cli'):
        self.mode = mode.lower()
        
        if self.mode == 'cli':
            self._init_local()
        elif self.mode == 'web':
            self._init_cloud()
        else:
            raise ValueError("Modo inválido. Use 'cli' ou 'web'.")

    def _init_local(self):
        """Conecta ao servidor Ollama local."""
        import ollama
        try:
            # Testa a conexão com o servidor
            ollama.list()
            print("✅ [CLI] Conectado ao servidor Ollama local (qwen2.5:3b).")
        except Exception as e:
            raise ConnectionError("Ollama server não está rodando. Execute 'ollama serve' no terminal.")

    def _init_cloud(self):
        """Conecta à API Groq (Nuvem)."""
        from groq import Groq
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY não encontrada no .env")
            
        self.client = Groq(api_key=api_key)
        print("✅ [WEB] Conectado à Groq API (Modelo: llama3-70b-8192).")

    def generate(self, user_prompt, system_prompt, history=None):
        """Gera uma resposta baseada no modo ativo."""
        if self.mode == 'cli':
            return self._generate_local(user_prompt, system_prompt, history)
        elif self.mode == 'web':
            return self._generate_cloud(user_prompt, system_prompt, history)

    def _generate_local(self, user_prompt, system_prompt, history):
        """Inferência via Ollama Local."""
        import ollama
        
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_prompt})

        response = ollama.chat(
            model='qwen2.5:1.5b',
            messages=messages,
            stream=False,
            options={"temperature": 0.1, "num_ctx": 512}
        )
        return response['message']['content'].strip()

    def _generate_cloud(self, user_prompt, system_prompt, history):
        """Inferência via Groq API."""
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_prompt})

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.3,
            max_tokens=1024
        )
        return response.choices[0].message.content.strip()
