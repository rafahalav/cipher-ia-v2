# 🛡️ CIPHER IA v2 - Cybersecurity Expert Assistant

[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Local_AI-Ollama-orange.svg)](https://ollama.ai/)
[![Groq API](https://img.shields.io/badge/Cloud_AI-Groq_120B-purple.svg)](https://groq.com/)

**Assistente de Cibersegurança com Arquitetura Híbrida: Modelo Local Leve (CLI) + Nuvem Pesada (Web)**

---

## 🎯 Sobre o Projeto

O **CIPHER IA** é um assistente especializado em cibersegurança projetado para operar em **hardware limitado** (CPUs antigas, 8GB RAM) sem comprometer a inteligência. Utilizando uma **arquitetura híbrida inovadora**, o sistema delega tarefas leves para inferência local (Ollama + Qwen2.5 1.5B) e análises complexas para a nuvem (Groq API + modelo 120B parâmetros).

### 🏗️ Por Que Arquitetura Híbrida?

A maioria dos projetos de IA assume hardware moderno (GPUs dedicadas, 32GB+ RAM). O CIPHER IA foi projetado para **democratizar o acesso a IA especializada** em máquinas com recursos limitados:

| Componente | Hardware Típico | Solução CIPHER |
|---|---|---|
| **CPU** | Intel i5 1ª geração (2010) | Ollama otimizado para CPU |
| **RAM** | 8GB (sistema + IA) | Modelo local 1.5B (~1.2GB) |
| **GPU** | Nenhuma (integrated only) | Inferência via Groq Cloud |
| **Resultado** | Travamentos com modelos 8B+ | Performance estável + inteligência sênior |

---

## ✨ Features

### 🔧 Modo CLI (Terminal)
- **Inferência Local**: Qwen2.5 1.5B via Ollama (zero latência de rede)
- **Execução de Comandos**: Diagnóstico de sistema em tempo real
- **Interface Rich**: Painéis coloridos, tabelas e estética cyberpunk
- **Segurança em Camadas**: Lista negra de comandos perigosos + validação de prompt

### 🌐 Modo Web (Navegador)
- **Inferência na Nuvem**: Groq API com modelo 120B parâmetros
- **Zero Carga Local**: CPU fria, RAM livre, sem superaquecimento
- **Análise CVSS**: Classificação de vulnerabilidades no padrão indústria
- **Exportação de Comandos**: Blocos de código Bash prontos para copiar

### 🛡️ Especialização em Cibersegurança
- **Mentalidade Red Team + Blue Team**: Ofensiva e defensiva
- **Classificação CVSS**: 🔴 CRÍTICO | 🟠 ALTO | 🟡 MÉDIO | 🟢 BAIXO
- **Framework MITRE ATT&CK**: Mapeamento de vetores de ataque
- **OWASP Top 10**: Análise de vulnerabilidades web
- **Hardening Linux**: Recomendações de segurança para sistemas

---

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.13+
- [Ollama](https://ollama.ai/) instalado
- Conta na [Groq](https://console.groq.com/) com API Key

### 1. Clone o Repositório
```bash
git clone https://github.com/rafahalav/cipher-ia-v2.git
cd cipher-ia-v2
```

### 2. Configure o Ambiente
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Baixar modelo local (2GB)
ollama pull qwen2.5:1.5b
```

### 3. Configure a API Key
Crie um arquivo `.env` na raiz do projeto:
```env
GROQ_API_KEY=gsk_sua_chave_aqui
```
Obtenha sua chave em: [https://console.groq.com/keys](https://console.groq.com/keys)

### 4. Execute
```bash
# Modo Terminal (CLI)
./start.sh

# Modo Navegador (Web)
./start.sh web
```

---

## 💬 Exemplos de Uso

### 🔧 Modo Diagnóstico (CLI)
**Entrada:**
```
Operador> verifique portas abertas no meu sistema
```

**Saída:**
```
⚙️ Comando de diagnóstico: ss -tulnp
┌─────────────────────────────────────────┐
│ SYSTEM OUTPUT                           │
├─────────────────────────────────────────┤
│ State   Recv-Q  Send-Q  Local Address   │
│ LISTEN  0       128     0.0.0.0:22      │
│ LISTEN  0       128     0.0.0.0:80      │
└─────────────────────────────────────────┘
```

### 🛡️ Modo Análise de Vulnerabilidade (Web)
**Entrada:**
```
Operador> meu servidor SSH está na porta 22 padrão e permite login direto como root. Analise isso.
```

**Saída:**
```
🔍 VETOR DE ATAQUE: Atacantes podem usar força bruta ou credenciais vazadas 
   para acessar o sistema diretamente como root, obtendo controle total.

⚠️ CRITICIDADE: 🟠 ALTO (CVSS 7.5) - Comprometimento significativo do sistema

💥 IMPACTO: 
   - Confidencialidade: Total (acesso a todos os dados)
   - Integridade: Total (modificação de arquivos do sistema)
   - Disponibilidade: Total (possibilidade de desligar o servidor)

🛡️ MITIGAÇÃO:
   1. Desabilite login root direto:
      EXECUTE: sudo sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
   2. Use autenticação por chave SSH:
      EXECUTE: ssh-keygen -t ed25519
   3. Mude a porta padrão:
      EXECUTE: sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
   4. Reinicie o serviço:
      EXECUTE: sudo systemctl restart sshd

📚 REFERÊNCIA: CWE-255 (Credentials Management), OWASP-A07:2021
```

### 💬 Modo Consulta Técnica (Web)
**Entrada:**
```
Operador> o que é um ataque de força bruta e como mitigar?
```

**Saída:**
```
Um ataque de força bruta (brute-force) consiste em tentar, de forma sistemática, 
todas as combinações possíveis de credenciais (usuário/senha, chaves criptográficas) 
até encontrar uma que conceda acesso ao recurso alvo.

É um método de adivinhação que depende exclusivamente da entropia (complexidade) 
das credenciais e da capacidade de tentativa do atacante (velocidade de envio de 
requisições, paralelismo, botnet, GPU, etc.).

**Tipos comuns:**
- Password-spraying: tenta poucas senhas comuns em muitos usuários
- Credential stuffing: usa credenciais vazadas de outros serviços
- Dictionary attack: usa listas de senhas pré-compiladas

**Mitigações:**
1. Autenticação multifator (MFA)
2. Rate limiting e bloqueio após tentativas falhas
3. Senhas longas e complexas (16+ caracteres)
4. Monitoramento de logs de autenticação
```

---

## 🧠 Arquitetura Técnica

### Fluxo de Inferência Híbrida
```
┌─────────────────────────────────────────────────────────────┐
│                    CIPHER IA v2                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐         ┌──────────────────────┐        │
│  │   CLI Mode   │         │    Web Mode          │        │
│  │  (Terminal)  │         │   (Navegador)        │        │
│  └──────┬───────┘         └──────────┬───────────┘        │
│         │                            │                     │
│         ▼                            ▼                     │
│  ┌──────────────┐         ┌──────────────────────┐        │
│  │  Ollama API  │         │    Groq API          │        │
│  │  (Localhost) │         │   (Cloud)            │        │
│  └──────┬───────┘         └──────────┬───────────┘        │
│         │                            │                     │
│         ▼                            ▼                     │
│  ┌──────────────┐         ┌──────────────────────┐        │
│  │ Qwen2.5 1.5B   │         │  Modelo 120B         │        │
│  │  (~2.5GB)    │         │  (Zero RAM local)    │        │
│  └──────────────┘         └──────────────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Decisões de Engenharia

| Decisão | Justificativa |
|---|---|
| **Ollama vs llama-cpp-python** | Ollama gerencia memória automaticamente, API padronizada, suporte a múltiplos modelos |
| **Qwen2.5 1.5B (local)** | Sweet spot: inteligente o suficiente para comandos EXECUTE:, leve para 8GB RAM |
| **Groq 120B (nuvem)** | Inteligência sênior para análises CVSS complexas, zero carga local |
| **System Prompt externo** | Separação de responsabilidades, fácil manutenção e teste de diferentes personas |
| **Lista negra de comandos** | Defesa em profundidade: mesmo que o modelo alucine, o código bloqueia |

---

## 📊 Por Que Isso Importa para AI Training?

Empresas como **Scale AI**, **Outlier** e **DataAnnotation** buscam profissionais que entendam:

1. **Arquitetura de Sistemas de IA**: Não apenas usar modelos, mas projetar sistemas completos
2. **Otimização de Recursos**: Trabalhar com restrições reais de hardware
3. **Segurança em IA**: Implementar guardrails, validação de output, proteção de credenciais
4. **Engenharia de Prompt**: Criar prompts que funcionam em modelos de diferentes tamanhos
5. **Domínio Especializado**: Aplicar IA em contextos específicos (cibersegurança, medicina, direito)

O CIPHER IA demonstra **todas essas competências** em um projeto funcional e documentado.

---

## 🛠️ Stack Tecnológica

- **Python 3.13**: Linguagem principal
- **Ollama**: Servidor de inferência local
- **Groq API**: Inferência na nuvem (modelo 120B)
- **Streamlit**: Interface web interativa
- **Rich**: Formatação avançada de terminal
- **python-dotenv**: Gerenciamento seguro de variáveis de ambiente

---

## 📁 Estrutura do Projeto

```
cipher-ia-v2/
├── core/
│   ├── __init__.py
│   └── llm_engine.py          # Motor de inferência híbrido
├── prompts/
│   └── system_prompt.txt      # Prompt sênior de cibersegurança
├── cli.py                      # Interface terminal (Rich)
├── web.py                      # Interface web (Streamlit)
├── start.sh                    # Lançador unificado
├── requirements.txt            # Dependências Python
├── .env                        # API Keys (NÃO commitar)
├── .gitignore                  # Proteção de arquivos sensíveis
└── README.md                   # Este arquivo
```

---

## 🔗 Projetos Relacionados

- **PAI AI Coder**: Assistente de geração de código Python - [github.com/rafahalav/pai-ai-coder](https://github.com/rafahalav/pai-ai-coder)
- **PAI Code Reviewer**: Analisador de código com foco em segurança e performance - [github.com/rafahalav/pai-code-reviewer](https://github.com/rafahalav/pai-code-reviewer)

---

## 👨‍💻 Autor

**Rafael Halav**  
Technology Professional | Telecommunications | IT | Python | AI | Data  
🔗 [LinkedIn](https://www.linkedin.com/in/rafael-halav) | ✉️ [Contato](mailto:rafa.halav83@gmail.com)

*Desenvolvido com foco em aprendizado contínuo e aplicação prática de Inteligência Artificial em cenários de recursos limitados.*

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

**Status**: Active Development  
**Última atualização**: Novembro 2026
```
# CIPHER IA v2
