#!/usr/bin/env python3
# ============================================
#   🛡️  CIPHER IA v2 - Interface Terminal (Rich)
#   Especialista em Cibersegurança
# ============================================

import sys
import os
import subprocess
import datetime
import platform
import time

# Adiciona a raiz do projeto ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from core.llm_engine import CipherEngine

console = Console()

# --- Configurações de Segurança (Camada 2) ---
COMANDOS_BLOQUEADOS = [
    "rm -rf", "shred", "wipe", "dd if", "mkfs", "fdisk", "parted",
    "shutdown", "reboot", "halt", "init 0", "poweroff",
    "iptables -f", "ufw disable", "systemctl stop firewalld",
    "chmod 777", "chown -r root:root /",
    "curl | bash", "wget | sh",
    "/dev/sd"
]

# --- Funções Visuais (Estética Cyberdeck) ---

def mostrar_banner():
    banner = """
    ╔══════════════════════════════════════════╗
    ║   🛡️  CIPHER IA - Cybersecurity Expert  ║
    ║   Powered by Qwen2.5 3B (Local)         ║
    ╚══════════════════════════════════════════╝
    """
    console.print(Panel(banner, title="[bold magenta]SYSTEM BOOT[/bold magenta]", border_style="cyan", expand=False))

def mostrar_ajuda():
    table = Table(title="[bold cyan]📋 Protocolos de Comando[/bold cyan]", border_style="green")
    table.add_column("Comando", style="bold yellow", width=20)
    table.add_column("Função", style="white")
    
    table.add_row("ajuda", "Mostra este painel de ajuda")
    table.add_row("hora / data", "Sincronização temporal")
    table.add_row("sistema", "Diagnóstico de hardware")
    table.add_row("limpar", "Limpar buffer da tela")
    table.add_row("limpar_memoria", "Resetar contexto neural")
    table.add_row("sair", "Desligar sistema")
    
    console.print(table)
    console.print("\n[dim]💡 Exemplos: 'verifique portas abertas', 'analise vulnerabilidades SSH', 'o que é SQL injection?'[/dim]\n")

def mostrar_hora():
    agora = datetime.datetime.now()
    console.print(Panel(f"[bold white]{agora.strftime('%H:%M:%S')}[/bold white]", title="🕐 Temporal Sync", border_style="blue", expand=False))

def mostrar_data():
    agora = datetime.datetime.now()
    dias = {"Monday": "Segunda", "Tuesday": "Terça", "Wednesday": "Quarta", 
            "Thursday": "Quinta", "Friday": "Sexta", "Saturday": "Sábado", "Sunday": "Domingo"}
    dia_pt = dias.get(agora.strftime("%A"), agora.strftime("%A"))
    console.print(Panel(f"[bold white]{agora.strftime('%d/%m/%Y')} ({dia_pt})[/bold white]", title="📅 Calendário", border_style="blue", expand=False))

def mostrar_sistema():
    table = Table(title="[bold cyan]💻 Diagnóstico de Hardware[/bold cyan]", border_style="magenta")
    table.add_column("Componente", style="bold yellow")
    table.add_column("Status", style="white")
    
    table.add_row("Sistema Operacional", f"{platform.system()} {platform.release()}")
    table.add_row("Arquitetura", platform.machine())
    table.add_row("Processador", platform.processor() or "Detectando...")
    table.add_row("Python Core", platform.python_version())
    table.add_row("Núcleo IA", "Qwen2.5 3B (Ollama Local)")
    
    console.print(table)

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')
    mostrar_banner()

# --- Lógica Principal da IA ---

def processar_entrada(entrada_usuario, engine, system_prompt, historico):
    """Processa a entrada, chama a IA e executa comandos se necessário."""
    console.print("\n[bold yellow]🛡️ Analisando através de lentes de segurança...[/bold yellow]")
    
    # Chama o motor de inferência
    resposta = engine.generate(entrada_usuario, system_prompt, historico)
    
    # Verifica se é um comando de execução
    if resposta.upper().startswith("EXECUTE:"):
        # Limpa o prefixo e pega apenas a primeira linha
        comando = resposta.split('\n')[0].replace("EXECUTE:", "").strip()
        
        # Verificação de segurança (Camada 2)
        if any(bloq in comando.lower() for bloq in COMANDOS_BLOQUEADOS):
            console.print(Panel("[bold red]🛡️ ACESSO NEGADO: Comando bloqueado por política de segurança do CIPHER.[/bold red]", border_style="red", expand=False))
            return

        console.print(f"\n[bold yellow]⚙️ Comando de diagnóstico:[/bold yellow] [white]{comando}[/white]")
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True, timeout=10)
            
            if resultado.returncode == 0:
                saida = resultado.stdout.strip()
                if not saida:
                    console.print("[dim](Execução bem-sucedida, sem retorno de dados)[/dim]")
                else:
                    console.print(Panel(f"[green]{saida}[/green]", title="[bold red]SYSTEM OUTPUT[/bold red]", border_style="red"))
            else:
                console.print(Panel(f"[red]{resultado.stderr.strip()}[/red]", title="❌ KERNEL ERROR", border_style="red", expand=False))
                
        except subprocess.TimeoutExpired:
            console.print("[bold red]⏱️ TIMEOUT: O processo excedeu o limite de 10 segundos.[/bold red]")
        except Exception as e:
            console.print(f"[bold red]❌ FALHA CRÍTICA: {e}[/bold red]")
            
    else:
        # Resposta textual (análise de vulnerabilidade ou consulta técnica)
        console.print(Panel(f"[white]{resposta}[/white]", title="[bold cyan]🛡️ CIPHER SECURITY ANALYSIS[/bold cyan]", border_style="magenta"))

# --- Programa Principal ---

def main():
    limpar_tela()
    
    # Carrega o System Prompt
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_dir, "prompts", "system_prompt.txt")
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            system_prompt = f.read()
    except FileNotFoundError:
        console.print("[bold red]❌ Erro: system_prompt.txt não encontrado em prompts/[/bold red]")
        sys.exit(1)

    # Inicializa o Motor (Modo CLI = Ollama Local)
    try:
        engine = CipherEngine(mode='cli')
    except Exception as e:
        console.print(f"[bold red]❌ Falha ao inicializar o núcleo neural: {e}[/bold red]")
        console.print("[yellow]💡 Verifique se o Ollama está rodando: ollama serve &[/yellow]")
        sys.exit(1)

    intro = """
    Olá, Operador. Eu sou o CIPHER IA.
    Especialista em Cibersegurança e Análise de Vulnerabilidades.
    Mentalidade: Red Team + Blue Team | Padrão: CVSS
    
    Digite 'ajuda' para ver os protocolos disponíveis.
    """
    console.print(Panel(intro, title="[bold green]BEM-VINDO AO CYBERDECK[/bold green]", border_style="green"))
    
    historico_conversa = []
    
    while True:
        try:
            entrada = console.input("[bold green]Operador> [/bold green]").strip()
            if not entrada:
                continue
            
            comando = entrada.lower()
            
            if comando == "sair":
                console.print("\n[bold red]🛑 Desligando sistemas de segurança... Até logo.[/bold red]\n")
                time.sleep(1)
                break
            elif comando == "ajuda":
                mostrar_ajuda()
            elif comando == "limpar_memoria":
                historico_conversa = []
                console.print("\n[bold yellow]🧹 Memória de contexto limpa.[/bold yellow]\n")
            elif comando == "hora":
                mostrar_hora()
            elif comando == "data":
                mostrar_data()
            elif comando == "sistema":
                mostrar_sistema()
            elif comando == "limpar":
                limpar_tela()
            else:
                # Adiciona ao histórico e processa
                historico_conversa.append({"role": "user", "content": entrada})
                if len(historico_conversa) > 8:
                    historico_conversa = historico_conversa[-8:]
                
                processar_entrada(entrada, engine, system_prompt, historico_conversa)
        
        except KeyboardInterrupt:
            console.print("\n\n[bold red]🛑 Interrupção manual detectada. Encerrando.[/bold red]\n")
            break
        except Exception as e:
            console.print(f"\n[bold red]❌ Erro inesperado no núcleo: {e}[/bold red]\n")

if __name__ == "__main__":
    main()
