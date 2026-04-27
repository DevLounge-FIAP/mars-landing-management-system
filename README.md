# 🚀 MGPEB - Sistema de Gerenciamento de Pouso e Estabilização de Base

[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Versão](https://img.shields.io/badge/Versão-2.0-orange)]()
[![Licença](https://img.shields.io/badge/Licença-FIAP-red)]()

> **Projeto Acadêmico - Missão Aurora Siger**  
> Sistema embarcado de simulação logística e aproximação orbital para colonização marciana.

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Características](#-características)
- [Arquitetura](#-arquitetura)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estruturas de Dados](#-estruturas-de-dados)
- [Algoritmos](#-algoritmos)
- [Equipe](#-equipe)
- [Documentação](#-documentação)

---

## 🎯 Visão Geral

O **MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base)** é um sistema de simulação que gerencia o pouso automatizado de 5 módulos espaciais em Marte, implementando decisões logísticas críticas baseadas em:

- **Lógica Booleana**: Portas AND para validação de segurança
- **Algoritmos de Otimização**: Bubble Sort e Busca Linear
- **Estruturas de Dados**: Filas FIFO, Listas e Objetos
- **Protocolo FAIL-SAFE**: Segurança por padrão "não autorizar"

### Objetivo Educacional

Demonstrar a aplicação prática de conceitos fundamentais de engenharia de software em um contexto realista de sistemas críticos espaciais, enfatizando:

✅ Modularização e separação de responsabilidades  
✅ Algoritmos e complexidade computacional  
✅ Estruturas de dados apropriadas  
✅ Testes unitários abrangentes  
✅ Boas práticas de documentação  

---

## ⭐ Características

### 🔐 Segurança em Primeiro Lugar
- **Protocolo FAIL-SAFE**: Estado padrão = "Não Autorizar Pouso"
- **Validação em 3 Camadas**: Combustível + Vento + Pista
- **Detecção de Emergência**: Identifica módulos críticos automaticamente

### 🎯 Processamento Priorizado
- **Fila FIFO**: Processamento justo e previsível
- **Ordenação por Prioridade**: Bubble Sort com reordenação dinâmica
- **Hierarquia Clara**: 5 módulos com níveis de criticidade

### 📊 Relatórios Detalhados
- Status em tempo real de cada pouso
- Diagnóstico de falhas
- Alertas de emergência
- Resumo consolidado pós-simulação

### 🧪 Qualidade Garantida
- 16+ testes unitários
- Cobertura de casos normais e exceções
- Validação de algoritmos e lógica de negócio

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                     PROGRAMA PRINCIPAL                      │
│                      (Aelton - main.py)                     │
│  - Orquestração do fluxo                                    │
│  - Gerenciamento de filas FIFO                              │
│  - Interface com usuário                                    │
└───────────────┬──────────────────────────┬──────────────────┘
                │                          │
        ┌───────▼────────┐         ┌───────▼───────┐
        │   ESTRUTURAS   │         │     LÓGICA    │
        │   (Victor)     │         │    (Bruno)    │
        │                │         │               │
        │ • Classe Modulo│         │ • Portas AND  │
        │ • 5 Módulos    │         │ • Bubble Sort │
        │ • Banco Dados  │         │ • Busca Linear│
        │                │         │ • Relatórios  │
        └────────────────┘         └───────────────┘
```

### Componentes Principais

#### 1. **Modelagem de Dados** (`src/structures/` - Victor)
- `modulo.py`: Classe `Modulo` representando módulos espaciais
- Atributos: ID, tipo, prioridade, combustível, massa, criticidade
- Métodos: validação de combustível crítico e estado de emergência

#### 2. **Lógica de Decisão** (`src/logic/` - Bruno)
- `logica_pouso.py`: Algoritmos e tomada de decisão
- Funções especializadas para cada aspecto da lógica
- Implementação da equação booleana: **A = C ∧ W ∧ P**

#### 3. **Banco de Dados** (`data/` - Victor)
- `modulos_dados.py`: 5 módulos oficiais da missão
- Dados estruturados e reutilizáveis
- Importação centralizada

#### 4. **Orquestração** (`src/` - Aelton)
- `main.py`: Programa principal que integra todos os componentes
- Gerencia fluxo de execução e interações entre camadas
- Interface com o usuário

#### 5. **Testes** (`tests/` - Aelton)
- `test_dados.py`: Suite de testes abrangente
- Validação de cada camada independentemente
- 16+ testes com cenários variados

---

## 📁 Estrutura do Projeto

```
mars-landing-management-system/
├── README.md                              # Este arquivo
├── requirements.txt                       # Dependências Python
├── CONSOLIDACAO.md                        # Documentação técnica da refatoração
│
├── src/                                   # Código-fonte principal
│   ├── main.py                           # Programa principal (Aelton)
│   ├── __init__.py
│   │
│   ├── structures/                        # Camada de Modelagem (Victor)
│   │   ├── modulo.py                     # Classe Modulo
│   │   └── __init__.py
│   │
│   └── logic/                             # Camada de Lógica (Bruno)
│       ├── logica_pouso.py               # Algoritmos e decisão
│       └── __init__.py
│
├── data/                                  # Banco de Dados (Victor)
│   ├── modulos_dados.py                  # 5 módulos da missão
│   └── __init__.py
│
├── tests/                                 # Testes Unitários (Aelton)
│   ├── test_dados.py                     # Suite completa de testes
│   └── __init__.py
│
└── venv/                                  # Ambiente virtual Python
    └── [dependências instaladas]
```

---

## 📦 Requisitos

- **Python**: 3.8 ou superior
- **Sistema Operacional**: Windows, macOS, Linux
- **Dependências**: Apenas biblioteca padrão do Python (sem dependências externas)

---

## 🚀 Instalação

### 1. Clone o Repositório
```bash
git clone https://github.com/DevLounge-FIAP/mars-landing-management-system.git
cd mars-landing-management-system
```

### 2. Crie um Ambiente Virtual (Recomendado)
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale Dependências (se houver)
```bash
pip install -r requirements.txt
```

---

## 💻 Como Usar

### Executar a Simulação Principal

```bash
python src/main.py
```

**Entrada Esperada:**
```
Digite a velocidade do vento registrada nos sensores (km/h): 50
```

**Saída:** Simulação completa com status de cada módulo e relatório final.

### Executar Testes Unitários

```bash
python tests/test_dados.py
```

**Esperado:** Todos os 16+ testes passam com sucesso.

### Exemplos de Execução

#### Simulação com Vento Favorável (50 km/h)
```bash
$ python src/main.py
Digite a velocidade do vento registrada nos sensores (km/h): 50
[Vento Marciano: 50 km/h]
[Modulos para processar: 5]
...
[OK] Modulos Pousados com Sucesso: 2-3
```

#### Simulação com Vento Desfavorável (90 km/h)
```bash
$ python src/main.py
Digite a velocidade do vento registrada nos sensores (km/h): 90
[Vento Marciano: 90 km/h]
...
ABORTAR: Condições climáticas inadequadas
```

---

## 🧠 Estruturas de Dados

### 1. Fila FIFO (First In, First Out)

**Utilização**: Processamento de módulos em sequência justa.

```python
# Implementação
fila_aproximacao = list(MODULOS)           # Cria fila
modulo = fila_aproximacao.pop(0)           # Remove primeiro (FIFO)
```

**Vantagens**:
- Ordem previsível e justa
- Complexidade O(n) para remoção
- Garante que nenhum módulo "pule" a fila

### 2. Lista Simples

**Utilização**: Armazenamento de módulos pousados e em espera.

```python
lista_pousados = []         # Módulos com sucesso
lista_espera = []           # Módulos aguardando
lista_pousados.append(m)    # Adiciona módulo
```

**Vantagens**:
- Acesso rápido por índice O(1)
- Operações flexíveis (append, remove, iterate)
- Adequada para quantidade pequena de elementos

### 3. Classe Objeto (Modulo)

**Utilização**: Representação estruturada de módulos espaciais.

```python
class Modulo:
    def __init__(self, id_nome, tipo, prioridade, combustivel, 
                 massa, criticidade, chegada_orbita, descricao=""):
        self.id_nome = id_nome
        self.tipo = tipo
        self.prioridade = prioridade
        self.combustivel = combustivel
        # ...
```

**Vantagens**:
- Encapsulamento de dados
- Métodos especializados
- Reutilização e manutenibilidade

---

## 🔧 Algoritmos

### 1. Bubble Sort - Ordenação por Prioridade

**Função**: `ordenar_por_prioridade(fila)`  
**Complexidade**: O(n²)  
**Responsável**: Bruno  

```python
def ordenar_por_prioridade(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j].prioridade > fila[j + 1].prioridade:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila
```

**Comportamento**: Compara elementos adjacentes e troca se necessário. Repete até estar ordenado.

**Vantagens neste contexto**:
- Simples de entender e implementar
- Adequado para pequeno conjunto (5 módulos)
- Previsível e determinístico

---

### 2. Busca Linear - Detecção de Emergência

**Função**: `buscar_menor_combustivel(fila)`  
**Complexidade**: O(n)  
**Responsável**: Bruno  

```python
def buscar_menor_combustivel(fila):
    if not fila:
        return None
    modulo_critico = fila[0]
    for modulo in fila:
        if modulo.combustivel < modulo_critico.combustivel:
            modulo_critico = modulo
    return modulo_critico
```

**Comportamento**: Itera sobre todos os elementos, mantendo referência ao mínimo encontrado.

**Aplicação**: Identifica módulo com combustível crítico para acionamento de protocolo de emergência.

---

### 3. Lógica Booleana - Portas AND

**Função**: `verificar_seguranca(modulo, vento_kmh, pista_livre)`  
**Equação**: **A = C ∧ W ∧ P**  
**Responsável**: Bruno  

```
Onde:
  C = Combustível >= 25%       (Condição de Combustível)
  W = Vento < 80 km/h          (Condição Ambiental)
  P = Pista Livre              (Condição Orbital)
  A = Autorização de Pouso     (Resultado)
```

**Implementação**:
```python
c_ok = modulo.combustivel >= 25
w_ok = vento_kmh < 80
p_ok = pista_livre

if c_ok and w_ok and p_ok:
    return True  # Pouso autorizado
```

**Protocolo FAIL-SAFE**:
- Estado padrão: NÃO autorizar
- Requer TODAS as condições serem verdadeiras
- Falha em uma = negação imediata

---

## 📊 5 Módulos da Missão Aurora Siger

| ID | Tipo | Prioridade | Combustível | Criticidade | Status |
|---|---|---|---|---|---|
| **MED-01** | Médico | 1 (Máxima) | 25% | 5/5 | Crítico |
| **ENG-02** | Energia | 2 | 40% | 5/5 | Normal |
| **HAB-03** | Habitação | 3 | 30% | 4/5 | Normal |
| **LOG-04** | Logístico | 4 | **12%** ⚠️ | 2/5 | **CRÍTICO** |
| **LAB-05** | Laboratório | 5 (Mínima) | 50% | 1/5 | Seguro |

---

## 👥 Equipe

### Estrutura Organizacional

```
MISSÃO AURORA SIGER - MGPEB
│
├─ VICTOR (Modelagem do Cenário e Estruturas de Dados)
│  ├─ src/structures/modulo.py      (Classe Modulo)
│  └─ data/modulos_dados.py         (Banco de dados - 5 módulos)
│
├─ BRUNO (Lógica de Decisão e Portas Lógicas)
│  └─ src/logic/logica_pouso.py     (Algoritmos e decisão)
│     ├─ verificar_pista()
│     ├─ verificar_seguranca()      (Portas AND)
│     ├─ ordenar_por_prioridade()   (Bubble Sort)
│     ├─ buscar_menor_combustivel() (Busca Linear)
│     └─ gerar_relatorio_seguranca()
│
└─ AELTON (Engenharia de Software / Programação)
   ├─ src/main.py                   (Orquestração)
   └─ tests/test_dados.py           (Testes - 16+ casos)
```

### Responsabilidades Claras

- **Victor**: Modelagem de dados e estruturas, banco de dados
- **Bruno**: Algoritmos, lógica booleana, análise de segurança
- **Aelton**: Integração, orquestração, testes, qualidade

---

## 🧪 Testes

### Suite de Testes Abrangente

```
Total de Testes: 16+

[Victor - Estruturas]
✓ test_criacao_modulo
✓ test_combustivel_critico
✓ test_em_emergencia
✓ test_repr_modulo

[Victor - Banco de Dados]
✓ test_quantidade_modulos
✓ test_ids_unicos
✓ test_prioridades_sequenciais
✓ test_obter_modulo_por_id
✓ test_modulos_criticos
✓ test_atributos_obrigatorios

[Bruno - Algoritmos]
✓ test_bubble_sort
✓ test_busca_linear
✓ test_busca_fila_vazia

[Bruno - Lógica de Segurança]
✓ test_seguranca_autorizado
✓ test_seguranca_combustivel_critico
✓ test_seguranca_pista_obstruida
✓ test_seguranca_vento_critico
```

### Executar Testes

```bash
python tests/test_dados.py

# Saída esperada:
# ======================================================================
#           EXECUTANDO SUITE DE TESTES - SISTEMA MGPEB
# ======================================================================
# [OK] test_criacao_modulo passou
# [OK] test_combustivel_critico passou
# ...
# ======================================================================
#   [OK] TODOS OS TESTES PASSARAM COM SUCESSO!
# ======================================================================
```

---

## 📚 Documentação

### Documentos Adicionais

| Documento | Descrição |
|-----------|-----------|
| [CONSOLIDACAO.md](CONSOLIDACAO.md) | Documentação técnica da refatoração e modularização |
| [SEGUNDO_ENTREGAVEL_CODIGO.md](SEGUNDO_ENTREGAVEL_CODIGO.md) | Código-fonte completo comentado |
| [ANEXO_ESTRUTURAS_DADOS.md](ANEXO_ESTRUTURAS_DADOS.md) | Análise detalhada de estruturas e algoritmos |

### Docstrings no Código

Todas as funções e classes possuem docstrings detalhadas:

```python
def verificar_seguranca(modulo, vento_kmh, pista_livre):
    """
    Aplica lógica de portas AND para autorizar pouso.
    Equação: A = C ∧ W ∧ P (Combustível AND Vento AND Pista)
    
    Args:
        modulo: Objeto Modulo com combustível
        vento_kmh: Velocidade do vento em km/h
        pista_livre: Boolean indicando se pista está livre
    
    Returns:
        True se pouso autorizado, False caso contrário
    """
```

---

## 🎓 Conceitos Educacionais Demonstrados

### Engenharia de Software
- ✅ **Modularização**: Separação clara de responsabilidades
- ✅ **Reutilização**: Imports e interfaces bem definidas
- ✅ **Manutenibilidade**: Código limpo e documentado
- ✅ **Escalabilidade**: Arquitetura extensível

### Algoritmos e Estruturas
- ✅ **Bubble Sort**: O(n²) - Simples mas ineficiente para grandes dados
- ✅ **Busca Linear**: O(n) - Simples e adequado para dados pequenos
- ✅ **FIFO**: Fila com comportamento previsível
- ✅ **Objetos**: Encapsulamento de dados e comportamento

### Lógica e Segurança
- ✅ **Portas Lógicas**: Implementação de AND booleano
- ✅ **FAIL-SAFE**: Segurança por padrão
- ✅ **Validação em Camadas**: Múltiplos pontos de verificação

### Boas Práticas
- ✅ **Testes Unitários**: Cobertura abrangente
- ✅ **Documentação**: README, docstrings, comments
- ✅ **Versionamento**: Git e controle de mudanças

---

## 🔍 Fluxo de Execução Detalhado

```
INÍCIO
  │
  ├─→ [1] ENTRADA: Velocidade do vento (entrada do usuário)
  │
  ├─→ [2] INICIALIZAÇÃO: Cria cópia da fila com 5 módulos
  │
  ├─→ [3] ORDENAÇÃO: Bubble Sort por prioridade
  │       └─ Reordena fila: [1, 2, 3, 4, 5]
  │
  ├─→ [4] PROCESSAMENTO FIFO: Para cada módulo
  │       ├─ pop(0) remove primeiro da fila
  │       ├─ verificar_pista() - Simula radar (True/False aleatório)
  │       ├─ verificar_seguranca(modulo, vento, pista)
  │       │   └─ Testa: C ∧ W ∧ P
  │       └─ Resultado:
  │           ├─ Autorizado → lista_pousados
  │           └─ Negado → lista_espera
  │
  ├─→ [5] BUSCA LINEAR: buscar_menor_combustivel(lista_espera)
  │       └─ Identifica módulo crítico
  │
  ├─→ [6] RELATÓRIO: gerar_relatorio_seguranca()
  │       └─ Exibe status completo
  │
  └─→ FIM
```

---

## 💡 Exemplos de Saída

### Simulação Bem-Sucedida

```
======================================================================
            INICIANDO PROTOCOLO MGPEB - SIMULACAO DE POUSO
======================================================================

Digite a velocidade do vento registrada nos sensores (km/h): 50

[Vento Marciano: 50 km/h]
[Modulos para processar: 5]

[*] Ordenando fila por prioridade (Bubble Sort)...
[OK] Fila ordenada

======================================================================
                    PROCESSAMENTO DE FILAS (FIFO)
======================================================================

[1/5] Solicitacao de pouso: MED-01 (MEDICO)
     Combustivel: 25% | Prioridade: 1 | Criticidade: 5
--- CHECANDO RADAR ORBITAL ---
     [+] POUSO AUTORIZADO E CONCLUIDO

[2/5] Solicitacao de pouso: ENG-02 (ENERGIA)
     Combustivel: 40% | Prioridade: 2 | Criticidade: 5
--- CHECANDO RADAR ORBITAL ---
     [+] POUSO AUTORIZADO E CONCLUIDO

...

======================================================================
                   --- Relatorio Final de Pouso ---
======================================================================

[OK] Modulos Pousados com Sucesso: 3
     ['MED-01', 'ENG-02', 'HAB-03']

[!] Modulos em Espera/Alerta: 2
     ['LOG-04', 'LAB-05']

[EMERGENCIA] ACAO IMEDIATA NECESSARIA:
     LOG-04 possui apenas 12% de combustivel.
     Criticidade: 2/5
     Massa: 15000kg

======================================================================
```

---

## 🐛 Tratamento de Erros

O sistema implementa tratamento robusto de erros:

```python
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

## 📝 Licença

Projeto Acadêmico - FIAP  
Todos os direitos reservados para fins educacionais.

---

## 🤝 Contribuições

Este é um projeto de equipe finalizado. Para mais informações sobre as contribuições específicas, consulte [CONSOLIDACAO.md](CONSOLIDACAO.md).

---

## 📞 Contato e Suporte

- **Repositório**: https://github.com/DevLounge-FIAP/mars-landing-management-system
- **Projeto**: Missão Aurora Siger - Sistema MGPEB
- **Instituição**: FIAP (Faculdade de Informática e Administração Paulista)

---

## ✨ Status do Projeto

- ✅ Arquitetura modular implementada
- ✅ 16+ testes passando
- ✅ Documentação completa
- ✅ Código refatorado e otimizado
- ✅ Pronto para produção educacional

---

**Versão**: 2.0  
**Data de Atualização**: 27 de abril de 2026  
**Status**: ✓ Completo e Funcional

