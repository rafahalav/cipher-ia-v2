#!/bin/bash

echo "🛡️  CIPHER IA v2 - Iniciando sistemas..."

# 1. Verifica se o Ollama já está rodando
if ! pgrep -x "ollama" > /dev/null; then
    echo "⚙️  Servidor Ollama não detectado. Iniciando em background..."
    ollama serve > /dev/null 2>&1 &
    sleep 3 # Aguarda 3 segundos para o servidor subir
    echo "✅ Servidor Ollama iniciado."
else
    echo "✅ Servidor Ollama já está ativo."
fi

# 2. Ativa o ambiente virtual (caso não esteja ativo)
if [ -z "$VIRTUAL_ENV" ]; then
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
fi

# 3. Lança a interface (CLI ou Web)
if [ "$1" == "web" ]; then
    echo "🌐 Abrindo interface Web..."
    streamlit run web.py
else
    echo "💻 Abrindo interface Terminal (CLI)..."
    python cli.py
fi
