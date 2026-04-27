# SEGUNDO ENTREGÁVEL - CÓDIGO-FONTE MGPEB

**Projeto:** Sistema de Gerenciamento de Pouso e Estabilização de Base (MGPEB)  
**Missão:** Aurora Siger - FIAP  
**Equipe:** DevLounge-FIAP  
**Repositório:** https://github.com/DevLounge-FIAP/mars-landing-management-system

---

## CÓDIGO-FONTE PYTHON

### 1. modulo.py - Estrutura de Dados

```python
"""
Módulo de Estrutura de Dados - Classe Modulo
Responsável por: Victor (Modelagem do Cenário e Estruturas de Dados)
Componente central para representar módulos espaciais da Missão Aurora Siger.
"""


class Modulo:
    
    def __init__(self, id_nome, tipo, prioridade, combustivel, massa, 
                 criticidade, chegada_orbita, descricao=""):
        """Inicializa um novo módulo espacial."""
        self.id_nome = id_nome
        self.tipo = tipo
        self.prioridade = prioridade
        self.combustivel = combustivel
        self.massa = massa
        self.criticidade = criticidade
        self.chegada_orbita = chegada_orbita
        self.descricao = descricao
        self.pousado = False
    
    def __repr__(self):
        """Representação em string do módulo."""
        status = "✓ Pousado" if self.pousado else "⊘ Aguardando"
        return (f"Modulo({self.id_nome} - {self.tipo.upper()} | "
                f"Comb: {self.combustivel}% | {status})")
    
    def is_combustivel_critico(self, limite=25):
        """Verifica se combustível está em nível crítico."""
        return self.combustivel <= limite
    
    def is_em_emergencia(self):
        """Verifica se o módulo está em estado de emergência."""
        return self.is_combustivel_critico() or self.criticidade <= 2
```

---

### 2. logica_pouso.py - Algoritmos e Decisão

```python
"""
Módulo de Lógica de Decisão e Portas Lógicas
Responsável por: Bruno (Lógica de Decisão)

Equação Booleana: A = C ∧ W ∧ P
  - C = Combustível >= 25%
  - W = Vento < 80 km/h
  - P = Pista Livre
  - A = Autorização de Pouso

Protocolo FAIL-SAFE: Estado padrão = NÃO autorizar
"""

import random


def verificar_pista():
    """Simula leitura do radar orbital para verificar se a pista está livre."""
    print('--- CHECANDO RADAR ORBITAL ---')
    pista = random.choice([True, False])
    print(f'Resultado: {"[OK] Pista Livre" if pista else "[!] Pista Obstruida"}')
    return pista


def verificar_seguranca(modulo, vento_kmh, pista_livre):
    """Aplica lógica de portas AND para autorizar pouso."""
    c_ok = modulo.combustivel >= 25  # Combustível adequado
    w_ok = vento_kmh < 80            # Clima favorável
    p_ok = pista_livre                # Pista desobstruída
    
    if c_ok and w_ok and p_ok:
        return True
    
    if not c_ok:
        print(f"ALERTA: {modulo.id_nome} com combustível crítico ({modulo.combustivel}%).")
        return False
    
    if not p_ok:
        print(f"ABORTAR: Pista obstruída detectada para {modulo.id_nome}.")
        return False
    
    print(f"ABORTAR: Vento inadequado para {modulo.id_nome} (vento: {vento_kmh} km/h > 80 km/h).")
    return False


def buscar_menor_combustivel(fila):
    """Busca linear O(n) - encontra módulo com menor combustível."""
    if not fila:
        return None
    
    modulo_critico = fila[0]
    for modulo in fila:
        if modulo.combustivel < modulo_critico.combustivel:
            modulo_critico = modulo
    
    return modulo_critico


def ordenar_por_prioridade(fila):
    """Bubble Sort O(n²) - ordena módulos por prioridade (1=máxima)."""
    n = len(fila)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j].prioridade > fila[j + 1].prioridade:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    
    return fila


def gerar_relatorio_seguranca(modulos_pousados, modulos_espera, modulo_critico=None):
    """Gera relatório consolidado pós-simulação."""
    print("\n" + "=" * 70)
    print("--- Relatorio Final de Pouso ---".center(70))
    print("=" * 70)
    
    print(f"\n[OK] Modulos Pousados com Sucesso: {len(modulos_pousados)}")
    if modulos_pousados:
        ids = [m.id_nome for m in modulos_pousados]
        print(f"     {ids}")
    
    print(f"\n[!] Modulos em Espera/Alerta: {len(modulos_espera)}")
    if modulos_espera:
        ids = [m.id_nome for m in modulos_espera]
        print(f"     {ids}")
    
    if modulo_critico:
        print(f"\n[EMERGENCIA] ACAO IMEDIATA NECESSARIA:")
        print(f"     {modulo_critico.id_nome} com apenas {modulo_critico.combustivel}% de combustível.")
        print(f"     Criticidade: {modulo_critico.criticidade}/5 | Massa: {modulo_critico.massa}kg")
    
    print("=" * 70 + "\n")
```

---

### 3. modulos_dados.py - Banco de Dados

```python
"""
Banco de Dados de Módulos Espaciais - Missão Aurora Siger MGPEB
Responsável por: Victor (Modelagem do Cenário e Estruturas de Dados)
Contém a definição dos 5 módulos para colonização marciana.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from structures.modulo import Modulo


MODULOS = [
    # Prioridade 1 - MÓDULO MÉDICO
    Modulo(
        id_nome="MED-01",
        tipo="medico",
        prioridade=1,
        combustivel=25,
        massa=4500,
        criticidade=5,
        chegada_orbita=180,
        descricao="Módulo de suporte médico com equipamentos de diagnóstico, farmácia e centro cirúrgico."
    ),
    
    # Prioridade 2 - MÓDULO ENERGIA
    Modulo(
        id_nome="ENG-02",
        tipo="energia",
        prioridade=2,
        combustivel=40,
        massa=8000,
        criticidade=5,
        chegada_orbita=150,
        descricao="Unidade de geração e distribuição de energia com painéis solares e baterias de backup."
    ),
    
    # Prioridade 3 - MÓDULO HABITAÇÃO
    Modulo(
        id_nome="HAB-03",
        tipo="habitacao",
        prioridade=3,
        combustivel=30,
        massa=12000,
        criticidade=4,
        chegada_orbita=200,
        descricao="Módulo pressurizado para habitação com sistema de suporte à vida integrado."
    ),
    
    # Prioridade 4 - MÓDULO LOGÍSTICO (RISCO CRÍTICO)
    Modulo(
        id_nome="LOG-04",
        tipo="logistico",
        prioridade=4,
        combustivel=12,  # ⚠️ COMBUSTÍVEL CRÍTICO
        massa=15000,
        criticidade=2,
        chegada_orbita=120,
        descricao="Módulo de logística com rovers para exploração. ⚠️ COMBUSTÍVEL CRÍTICO - RISCO!"
    ),
    
    # Prioridade 5 - MÓDULO LABORATÓRIO
    Modulo(
        id_nome="LAB-05",
        tipo="laboratorial",
        prioridade=5,
        combustivel=50,
        massa=6000,
        criticidade=1,
        chegada_orbita=90,
        descricao="Laboratório pressurizável para experimentos científicos e pesquisa de sustentabilidade."
    ),
]


def obter_modulo_por_id(id_nome):
    """Retorna um módulo específico pelo ID."""
    for modulo in MODULOS:
        if modulo.id_nome == id_nome:
            return modulo
    return None
```

---

### 4. main.py - Orquestração Principal

```python
"""
MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base
Projeto: Missão Aurora Siger - FIAP

Atribuições:
  - Victor: Modelagem do Cenário e Estruturas de Dados
  - Bruno: Lógica de Decisão e Portas Lógicas  
  - Aelton: Engenharia de Software / Orquestração
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from data.modulos_dados import MODULOS
from src.logic import (
    verificar_pista,
    verificar_seguranca,
    buscar_menor_combustivel,
    ordenar_por_prioridade,
    gerar_relatorio_seguranca
)


def executar_simulacao():
    """Executa a simulação completa de pouso dos módulos."""
    
    print("\n" + "=" * 70)
    print("INICIANDO PROTOCOLO MGPEB - SIMULACAO DE POUSO".center(70))
    print("=" * 70 + "\n")
    
    try:
        vento_kmh = int(input('Digite a velocidade do vento registrada nos sensores (km/h): '))
    except ValueError:
        print("[!] Entrada invalida. Usando vento padrao: 50 km/h")
        vento_kmh = 50
    
    print(f"\n[Vento Marciano: {vento_kmh} km/h]")
    print(f"[Modulos para processar: {len(MODULOS)}]")
    
    fila_aproximacao = list(MODULOS)
    lista_pousados = []
    lista_espera = []
    
    print("\n[*] Ordenando fila por prioridade (Bubble Sort)...")
    fila_aproximacao = ordenar_por_prioridade(fila_aproximacao)
    print("[OK] Fila ordenada")
    
    print(f"\n{'=' * 70}")
    print("PROCESSAMENTO DE FILAS (FIFO)".center(70))
    print(f"{'=' * 70}\n")
    
    iteracao = 0
    while len(fila_aproximacao) > 0:
        iteracao += 1
        modulo_atual = fila_aproximacao.pop(0)
        
        print(f"\n[{iteracao}/{len(MODULOS)}] Solicitacao de pouso: {modulo_atual.id_nome} ({modulo_atual.tipo.upper()})")
        print(f"     Combustivel: {modulo_atual.combustivel}% | Prioridade: {modulo_atual.prioridade} | Criticidade: {modulo_atual.criticidade}")
        
        pista_livre_atual = verificar_pista()
        autorizado = verificar_seguranca(modulo_atual, vento_kmh, pista_livre_atual)
        
        if autorizado:
            print("     [+] POUSO AUTORIZADO E CONCLUIDO")
            modulo_atual.pousado = True
            lista_pousados.append(modulo_atual)
        else:
            print("     [!] POUSO NEGADO - Redirecionado para lista de espera")
            lista_espera.append(modulo_atual)
    
    print(f"\n{'=' * 70}")
    print("DETECCAO DE EMERGENCIA (BUSCA LINEAR)".center(70))
    print(f"{'=' * 70}\n")
    
    modulo_critico = buscar_menor_combustivel(lista_espera)
    
    if modulo_critico:
        print(f"[ALERTA] Modulo critico em espera detectado: {modulo_critico.id_nome}")
        print(f"         Combustivel: {modulo_critico.combustivel}%")
    else:
        print("[OK] Nenhum modulo critico detectado")
    
    print(f"\n{'=' * 70}")
    gerar_relatorio_seguranca(lista_pousados, lista_espera, modulo_critico)


if __name__ == "__main__":
    try:
        executar_simulacao()
    except KeyboardInterrupt:
        print("\n\n[!] Simulacao interrompida pelo usuario.")
    except Exception as e:
        print(f"\n[ERRO] Erro durante simulacao: {e}")
        import traceback
        traceback.print_exc()
```

---

## COMO EXECUTAR

### Executar Simulação Principal
```bash
python src/main.py
```

### Executar Testes Unitários  
```bash
python tests/test_dados.py
```
---

def test_dados_modulos():
    """Testa carregamento de dados dos módulos."""
    assert len(MODULOS) == 5
    
    # Verifica que cada módulo tem ID único
    ids = [m.id_nome for m in MODULOS]
    assert len(ids) == len(set(ids))
    
    # Verifica LOG-04 com combustível crítico
    log = obter_modulo_por_id("LOG-04")
    assert log.combustivel == 12
    assert log.is_combustivel_critico() == True
    
    print("✓ Test test_dados_modulos PASSED")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("EXECUTANDO SUITE DE TESTES".center(70))
    print("=" * 70 + "\n")
    
    test_modulo_combustivel_critico()
    test_modulo_emergencia()
    test_verificar_seguranca()
    test_buscar_menor_combustivel()
    test_ordenar_por_prioridade()
    test_dados_modulos()
    
    print("\n" + "=" * 70)
    print("TODOS OS TESTES PASSARAM COM SUCESSO!".center(70))
    print("=" * 70 + "\n")
```

---

## COMO EXECUTAR

### 1. Instalação

```bash
# Clone ou configure o workspace
cd c:\user\mars-landing-management-system

# Ative o ambiente virtual (se disponível)
.\venv\Scripts\Activate.ps1
```

### 2. Executar Simulação Principal

```bash
python src/main.py
```

Será solicitado: `Digite a velocidade do vento registrada nos sensores (km/h):`

Insira um valor entre 0-100 (exemplo: 50)

### 3. Executar Testes

```bash
python tests/test_dados.py
```

---

**Fim do Segundo Entregável - Código-Fonte**
