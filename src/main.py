"""
MÓDULO DE GERENCIAMENTO DE POUSO E ESTABILIZAÇÃO DE BASE (MGPEB)
Projeto: Missão Aurora Siger - FIAP

Sistema embarcado de simulação logística e aproximação orbital para colonização marciana.

╔═══════════════════════════════════════════════════════════════════════════════╗
║                          ATRIBUIÇÕES DO PROJETO                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║ Modelagem do Cenário e Estruturas de Dados - Victor                          ║
║   └─ data/modulos_dados.py: Definição dos 5 módulos                          ║
║   └─ src/structures/modulo.py: Classe Modulo                                 ║
║                                                                               ║
║ Lógica de Decisão e Portas Lógicas - Bruno                                   ║
║   └─ src/logic/logica_pouso.py: Algoritmos e decisão (AND, Bubble, Busca)   ║
║                                                                               ║
║ Engenharia de Software / Programação - Aelton                                ║
║   └─ src/main.py: Orquestração (este arquivo)                               ║
║   └─ tests/test_dados.py: Suite de testes                                    ║
║   └─ Integração modular e deployment                                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Execução:
    python src/main.py

Testes:
    python tests/test_dados.py
"""

import sys
from pathlib import Path

# Importações do projeto
# ─────────────────────────────────────────────────────────────────────────────

# Victor: Banco de dados dos módulos (Modelagem do Cenário)
sys.path.insert(0, str(Path(__file__).parent.parent))
from data.modulos_dados import MODULOS

# Bruno: Lógica de Decisão (Portas Lógicas e Algoritmos)
from src.logic import (
    verificar_pista,
    verificar_seguranca,
    buscar_menor_combustivel,
    ordenar_por_prioridade,
    gerar_relatorio_seguranca
)

# ─────────────────────────────────────────────────────────────────────────────
# PROGRAMA PRINCIPAL - Orquestração (Aelton)
# ─────────────────────────────────────────────────────────────────────────────


def executar_simulacao():
    """
    Executa a simulação completa de pouso dos módulos.
    
    Fluxo:
    1. Recebe velocidade do vento como entrada
    2. Ordena fila por prioridade (Bubble Sort)
    3. Processa cada módulo em fila FIFO
    4. Aplica lógica de segurança (portas AND)
    5. Gerencia pousados vs espera
    6. Identifica emergências
    7. Gera relatório final
    """
    
    print("\n" + "=" * 70)
    print("INICIANDO PROTOCOLO MGPEB - SIMULACAO DE POUSO".center(70))
    print("=" * 70 + "\n")
    
    # ─────────────────────────────────────────────────────────────────────────
    # 1. ENTRADA DE DADOS
    # ─────────────────────────────────────────────────────────────────────────
    try:
        vento_kmh = int(input('Digite a velocidade do vento registrada nos sensores (km/h): '))
    except ValueError:
        print("[!] Entrada invalida. Usando vento padrao: 50 km/h")
        vento_kmh = 50
    
    print(f"\n[Vento Marciano: {vento_kmh} km/h]")
    print(f"[Modulos para processar: {len(MODULOS)}]")
    
    # ─────────────────────────────────────────────────────────────────────────
    # 2. INICIALIZAÇÃO - Cria cópia da fila (Victor: dados originais)
    # ─────────────────────────────────────────────────────────────────────────
    fila_aproximacao = list(MODULOS)
    lista_pousados = []
    lista_espera = []
    
    # ─────────────────────────────────────────────────────────────────────────
    # 3. ORDENAÇÃO - Bubble Sort por Prioridade (Bruno)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n[*] Ordenando fila por prioridade (Bubble Sort)...")
    fila_aproximacao = ordenar_por_prioridade(fila_aproximacao)
    print("[OK] Fila ordenada")
    
    # ─────────────────────────────────────────────────────────────────────────
    # 4. PROCESSAMENTO - FIFO (Aelton: orquestração)
    # ─────────────────────────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("PROCESSAMENTO DE FILAS (FIFO)".center(70))
    print(f"{'=' * 70}\n")
    
    iteracao = 0
    while len(fila_aproximacao) > 0:
        iteracao += 1
        
        # Pop(0) implementa comportamento FIFO
        modulo_atual = fila_aproximacao.pop(0)
        
        print(f"\n[{iteracao}/{len(MODULOS)}] Solicitacao de pouso: {modulo_atual.id_nome} "
              f"({modulo_atual.tipo.upper()})")
        print(f"     Combustivel: {modulo_atual.combustivel}% | "
              f"Prioridade: {modulo_atual.prioridade} | "
              f"Criticidade: {modulo_atual.criticidade}")
        
        # Bruno: Verifica pista
        pista_livre_atual = verificar_pista()
        
        # Bruno: Aplica lógica de segurança (A = C ∧ W ∧ P)
        autorizado = verificar_seguranca(modulo_atual, vento_kmh, pista_livre_atual)
        
        # Aelton: Registra resultado
        if autorizado:
            print("     [+] POUSO AUTORIZADO E CONCLUIDO")
            modulo_atual.pousado = True
            lista_pousados.append(modulo_atual)
        else:
            print("     [!] POUSO NEGADO - Redirecionado para lista de espera")
            lista_espera.append(modulo_atual)
    
    # ─────────────────────────────────────────────────────────────────────────
    # 5. BUSCA DE EMERGÊNCIA (Bruno: Busca Linear)
    # ─────────────────────────────────────────────────────────────────────────
    emergencia = buscar_menor_combustivel(lista_espera)
    
    # ─────────────────────────────────────────────────────────────────────────
    # 6. RELATÓRIO FINAL
    # ─────────────────────────────────────────────────────────────────────────
    gerar_relatorio_seguranca(lista_pousados, lista_espera, emergencia)


# ─────────────────────────────────────────────────────────────────────────────
# PONTO DE ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        executar_simulacao()
    except KeyboardInterrupt:
        print("\n\n[!] Simulacao interrompida pelo usuario.")
    except Exception as e:
        print(f"\n[ERRO] Erro durante simulacao: {e}")
        import traceback
        traceback.print_exc()
