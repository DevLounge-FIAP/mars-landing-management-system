# Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
# Projeto: Missão Aurora Siger

import random

class Modulo:
    def __init__(self, id_nome, prioridade, combustivel, massa):
        self.id_nome = id_nome
        self.prioridade = prioridade  # 1 é a maior prioridade
        self.combustivel = combustivel # Porcentagem (0 a 100)
        self.massa = massa
        self.pousado = False
# Módulos definitos por Victor
# 1. Inicialização do Cenário
fila_aproximacao = [
    Modulo("MED-01", 1, 25, 4500),
    Modulo("ENG-02", 2, 40, 8000),
    Modulo("HAB-03", 3, 30, 12000),
    Modulo("LOG-04", 4, 12, 15000), # Combustível crítico
    Modulo("LAB-05", 5, 50, 6000)
]

lista_pousados = []
lista_espera = []

def verificar_pista():
    """Simula a leitura do radar para verificar se a pista está livre."""
    print('--- CHECANDO RADAR ORBITAL ---')
    return random.choice([True, False]) # Retorna True ou False aleatoriamente

def verificar_seguranca(modulo, vento, pista):
    """Aplica a lógica de portas AND para autorizar o pouso."""
    c_ok = modulo.combustivel > 10
    w_ok = vento < 80
    p_ok = pista
    
    #Lógica implementada por Bruno
    # Lógica If/Elif/Else   
    if c_ok and w_ok and p_ok:
        return True
    elif not c_ok:
        print(f"ALERTA: {modulo.id_nome} com combustível crítico ({modulo.combustivel}%).")
        return False
    elif not p_ok:
        print(f"ABORTAR: Pista obstruída detectada pelo radar para o módulo {modulo.id_nome}.")
        return False
    else:
        print(f"ABORTAR: Condições climáticas inadequadas para {modulo.id_nome}.")
        return False

def buscar_menor_combustivel(fila):
    """Algoritmo de Busca Linear para encontrar a maior emergência."""
    if not fila: 
        return None
    
    modulo_critico = fila[0]
    for modulo in fila:
        if modulo.combustivel < modulo_critico.combustivel:
            modulo_critico = modulo
    return modulo_critico

def ordenar_por_prioridade(fila):
    """Algoritmo de ordenação Bubble Sort para reorganizar a fila por prioridade."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j].prioridade > fila[j+1].prioridade:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# 2. Execução da Simulação
print("--- Iniciando Protocolo MGPEB ---")

# Variáveis de Ambiente Globais
vento_kmh = int(input('Digite a velocidade do vento registrada nos sensores (km/h): '))

# Etapa A: Ordenar fila por prioridade antes de iniciar os pousos
fila_aproximacao = ordenar_por_prioridade(fila_aproximacao)

# Etapa B: Processar Fila (FIFO)
while len(fila_aproximacao) > 0:
    # Pop(0) retira e retorna o primeiro elemento da lista (comportamento de Fila)
    modulo_atual = fila_aproximacao.pop(0)
    
    print(f"\nSolicitação de pouso recebida: {modulo_atual.id_nome}")
    
    # O radar faz uma nova leitura para CADA módulo na fila
    pista_livre_atual = verificar_pista() 
    
    autorizado = verificar_seguranca(modulo_atual, vento_kmh, pista_livre_atual)
    
    if autorizado:
        print(f">> Pouso autorizado e concluído: {modulo_atual.id_nome}")
        modulo_atual.pousado = True
        lista_pousados.append(modulo_atual)
    else:
        print(f">> Pouso negado. {modulo_atual.id_nome} enviado para lista de espera/alerta.")
        lista_espera.append(modulo_atual)

# Etapa C: Relatório Final
print("\n--- Relatório Final de Pouso ---")
print(f"Módulos Pousados de forma segura: {[m.id_nome for m in lista_pousados]}")
print(f"Módulos em Espera/Alerta: {[m.id_nome for m in lista_espera]}")

# Etapa D: Identificar emergência na lista de espera
emergencia = buscar_menor_combustivel(lista_espera)
if emergencia:
    print(f"\nAÇÃO IMEDIATA NECESSÁRIA: {emergencia.id_nome} possui apenas {emergencia.combustivel}% de combustível.")