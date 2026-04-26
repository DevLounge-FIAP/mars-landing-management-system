"""
MÓDULO DE LÓGICA DE DECISÃO E PORTAS LÓGICAS
Responsável por: Bruno (Lógica de Decisão)

Implementa a lógica booleana para autorização de pousos e algoritmos de otimização.
Define as regras de segurança, verificações ambientais e processamento de filas.

Equação Booleana Principal:
    A = C ∧ W ∧ P

Onde:
    C = Combustível > 10% (Variável de Segurança)
    W = Vento < 80 km/h (Variável Ambiental)
    P = Pista Livre (Variável Orbital)
    A = Autorização de Pouso
"""

import random


def verificar_pista():
    """
    Simula a leitura do radar orbital para verificar se a pista está livre.
    
    O sistema orbital de Mars realiza varredura de radar em tempo real para
    detectar obstruções na pista de pouso. A leitura é estocástica (aleatória)
    para simular variabilidade de condições atmosféricas marcianas.
    
    Returns:
        bool: True se pista está livre, False se detecta obstrução
    
    Ambiente: Marte - Raio orbital a 300 km de altitude
    Frequência: Novamente a cada solicitação de módulo
    """
    print('--- CHECANDO RADAR ORBITAL ---')
    return random.choice([True, False])


def verificar_seguranca(modulo, vento_kmh, pista_livre):
    """
    Aplica lógica de portas AND para autorizar pouso.
    
    Implementa a equação booleana de segurança com três variáveis críticas:
    
    Condição de Autorização (AND lógico):
        AUTORIZADO = (C > 10%) AND (W < 80 km/h) AND (P = True)
    
    Se qualquer condição falhar, o pouso é negado e o módulo é redirecionado
    para lista de espera ou alerta de emergência.
    
    Args:
        modulo (Modulo): Objeto do módulo solicitando pouso
        vento_kmh (int): Velocidade do vento marciano em km/h
        pista_livre (bool): Resultado da verificação orbital
    
    Returns:
        bool: True se todas as três condições são satisfeitas, False caso contrário
    
    Lógica:
        - C_OK: Combustível do módulo > 10% (margem de segurança)
        - W_OK: Velocidade do vento < 80 km/h (limite de estabilidade)
        - P_OK: Pista detectada como livre pelo radar orbital
    """
    # Variáveis booleanas da condição
    c_ok = modulo.combustivel > 10  # Combustível adequado
    w_ok = vento_kmh < 80            # Clima favorável
    p_ok = pista_livre                # Pista desobstruída
    
    # Porta AND: Todas as três condições devem ser verdadeiras
    if c_ok and w_ok and p_ok:
        return True
    
    # Se falha, reporta qual condição falhou
    if not c_ok:
        print(f"ALERTA: {modulo.id_nome} com combustível crítico ({modulo.combustivel}%).")
        return False
    
    if not p_ok:
        print(f"ABORTAR: Pista obstruída detectada pelo radar para o módulo {modulo.id_nome}.")
        return False
    
    # Vento fora dos limites
    print(f"ABORTAR: Condições climáticas inadequadas para {modulo.id_nome} "
          f"(vento: {vento_kmh} km/h > 80 km/h).")
    return False


def buscar_menor_combustivel(fila):
    """
    Algoritmo de Busca Linear para identificar emergência crítica.
    
    Implementa busca linear O(n) através da fila para encontrar o módulo
    com nível de combustível mais crítico (menor combustível restante).
    
    Este módulo é prioridade máxima para reavaliação, pois tem risco
    iminente de falha catastrófica.
    
    Args:
        fila (list): Lista de objetos Modulo para buscar
    
    Returns:
        Modulo: Objeto do módulo com menor combustível
        None: Se a fila está vazia
    
    Complexidade: O(n) - uma passagem linear
    """
    if not fila:
        return None
    
    modulo_critico = fila[0]
    for modulo in fila:
        if modulo.combustivel < modulo_critico.combustivel:
            modulo_critico = modulo
    
    return modulo_critico


def ordenar_por_prioridade(fila):
    """
    Algoritmo de Bubble Sort para reorganizar fila por prioridade.
    
    Implementa ordenação Bubble Sort O(n²) para reordenar os módulos
    de acordo com sua prioridade de pouso (1 = máxima, 5 = mínima).
    
    A reordenação garante que módulos críticos (ex: suporte médico, energia)
    sejam processados primeiro, mantendo coerência com prioridades
    definidas no cenário.
    
    Args:
        fila (list): Lista de objetos Modulo para ordenar
    
    Returns:
        list: Fila ordenada por prioridade (ordem crescente)
    
    Complexidade:
        - Pior caso: O(n²)
        - Melhor caso: O(n) se já está ordenada
    
    Nota: Para n=5 módulos (projeto atual), desempenho é negligenciável.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara prioridades e troca se necessário
            if fila[j].prioridade > fila[j + 1].prioridade:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    
    return fila


def gerar_relatorio_seguranca(modulos_pousados, modulos_espera, modulo_critico=None):
    """
    Gera relatório consolidado de segurança pós-simulação.
    
    Apresenta um resumo das decisões de pouso e identifica situações
    de emergência que requerem ação imediata.
    
    Args:
        modulos_pousados (list): Módulos que pousaram com sucesso
        modulos_espera (list): Módulos em espera ou com problemas
        modulo_critico (Modulo): Módulo identificado como crítico (opcional)
    """
    print("\n" + "=" * 70)
    print("--- Relatorio Final de Pouso ---".center(70))
    print("=" * 70)
    
    print(f"\n[OK] Modulos Pousados com Sucesso: {len(modulos_pousados)}")
    if modulos_pousados:
        print(f"     {[m.id_nome for m in modulos_pousados]}")
    
    print(f"\n[!] Modulos em Espera/Alerta: {len(modulos_espera)}")
    if modulos_espera:
        print(f"     {[m.id_nome for m in modulos_espera]}")
    
    if modulo_critico:
        print(f"\n[EMERGENCIA] ACAO IMEDIATA NECESSARIA:")
        print(f"     {modulo_critico.id_nome} possui apenas {modulo_critico.combustivel}% "
              f"de combustivel.")
        print(f"     Criticidade: {modulo_critico.criticidade}/5")
        print(f"     Massa: {modulo_critico.massa}kg")
    
    print("=" * 70 + "\n")
