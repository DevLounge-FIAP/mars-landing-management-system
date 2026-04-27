# ANEXO: ESTRUTURAS DE DADOS UTILIZADAS NO MGPEB

**Projeto:** Sistema de Gerenciamento de Pouso e Estabilização de Base (MGPEB)  
**Missão:** Aurora Siger - FIAP  
**Data:** Abril de 2026  
**Responsável:** Aelton (Engenharia de Software)

---

## 📚 ÍNDICE

1. [Introdução](#introdução)
2. [Estruturas Utilizadas](#estruturas-utilizadas)
   - 2.1 [Fila FIFO (First In, First Out)](#21-fila-fifo)
   - 2.2 [Lista Simples](#22-lista-simples)
   - 2.3 [Classe Objeto (Modulo)](#23-classe-objeto-modulo)
3. [Comparação com Pilhas](#comparação-com-pilhas)
4. [Análise de Complexidade](#análise-de-complexidade)
5. [Diagrama de Fluxo](#diagrama-de-fluxo)
6. [Exemplos Práticos](#exemplos-práticos)

---

## INTRODUÇÃO

O MGPEB utiliza estruturas de dados fundamentais para gerenciar o processamento dos 5 módulos espaciais. A escolha dessas estruturas reflete o design robusto e previsível necessário em sistemas críticos espaciais.

### Por que essas estruturas?

| Estrutura | Motivo da Escolha | Aplicação |
|-----------|------------------|-----------|
| **Fila FIFO** | Orden justa, previsível | Processamento de módulos em sequência |
| **Lista Simples** | Acesso aleatório, flexibilidade | Armazenamento de resultados (pousados, espera) |
| **Classe Objeto** | Abstração, integridade | Representação de módulos espaciais |

---

## ESTRUTURAS UTILIZADAS

### 2.1 Fila FIFO (First In, First Out)

#### Conceito Fundamental

Uma **Fila** (Queue) é uma estrutura linear onde:
- **Inserção:** Ocorre no final (enqueue/push)
- **Remoção:** Ocorre no início (dequeue/pop)
- **Princípio:** FIFO - Primeiro a entrar é primeiro a sair

```
Fila Inicial:
┌────────┬────────┬────────┬────────┬────────┐
│ MED-01 │ ENG-02 │ HAB-03 │ LOG-04 │ LAB-05 │
└────────┴────────┴────────┴────────┴────────┘
  ↑                                        ↑
Início (Saída)                           Fim (Entrada)

Após pop(0):
┌────────┬────────┬────────┬────────┐
│ ENG-02 │ HAB-03 │ LOG-04 │ LAB-05 │
└────────┴────────┴────────┴────────┘
```

#### Implementação no MGPEB

**Arquivo:** `src/main.py`  
**Função:** `executar_simulacao()`

```python
# Inicialização da fila FIFO
fila_aproximacao = list(MODULOS)  # Cria cópia da lista

# Processamento FIFO
while len(fila_aproximacao) > 0:
    # Pop(0) = Remove do início (comportamento FIFO)
    modulo_atual = fila_aproximacao.pop(0)
    
    # Processa módulo
    autorizado = verificar_seguranca(modulo_atual, vento_kmh, pista_livre)
    
    # Distribui para lista apropriada
    if autorizado:
        lista_pousados.append(modulo_atual)
    else:
        lista_espera.append(modulo_atual)
```

#### Características

| Propriedade | Valor |
|-------------|-------|
| **Operação de Inserção** | O(1) - append() |
| **Operação de Remoção** | O(n) - pop(0) em lista dinâmica |
| **Acesso Aleatório** | O(n) |
| **Espaço** | O(n) |
| **Uso Real** | Processamento de requisições em fila de espera |

#### Por que FIFO?

1. **Justiça:** Módulo que chegou primeiro é processado primeiro
2. **Previsibilidade:** Comportamento determinístico (crítico em missões)
3. **Simplicidade:** Fácil de implementar e debugar
4. **Transparência:** Nenhuma surpresa no algoritmo

---

### 2.2 Lista Simples

#### Conceito Fundamental

Uma **Lista** é uma coleção ordenada de elementos onde:
- **Inserção:** Pode ocorrer em qualquer posição - O(1) no final
- **Acesso:** Direto por índice - O(1)
- **Busca:** Linear - O(n)
- **Remoção:** Pode ocorrer em qualquer posição

```
Lista de Pousados:
┌────────┬────────┬────────┐
│ MED-01 │ HAB-03 │ LAB-05 │  ← Módulos com pouso aprovado
└────────┴────────┴────────┘
  [0]      [1]      [2]

Acesso direto: lista_pousados[1] = HAB-03
```

#### Implementação no MGPEB

**Arquivo:** `src/main.py`

```python
# Três listas para categorizar módulos
lista_pousados = []   # Módulos com pouso autorizado
lista_espera = []     # Módulos aguardando condições
lista_criticos = []   # Emergências detectadas

# Adição à lista (O(1))
if autorizado:
    lista_pousados.append(modulo_atual)
else:
    lista_espera.append(modulo_atual)

# Acesso direto (O(1))
primeiro_pousado = lista_pousados[0]

# Busca linear (O(n))
for modulo in lista_espera:
    if modulo.is_combustivel_critico():
        processar_emergencia(modulo)
```

#### Características

| Propriedade | Valor |
|-------------|-------|
| **Inserção (final)** | O(1) |
| **Inserção (posição)** | O(n) |
| **Remoção (final)** | O(1) |
| **Acesso por índice** | O(1) |
| **Busca** | O(n) |
| **Espaço** | O(n) |

#### Por que Listas?

1. **Flexibilidade:** Tamanho dinâmico
2. **Acesso Rápido:** Indexação O(1)
3. **Append Eficiente:** Inserção ao final é rápida
4. **Suporte Built-in:** Python oferece lista nativa otimizada

---

### 2.3 Classe Objeto (Modulo)

#### Conceito Fundamental

Uma **Classe** é uma estrutura de dados que agrupa:
- **Atributos:** Dados associados
- **Métodos:** Comportamentos

```python
Modulo
├── Atributos
│   ├── id_nome: str
│   ├── tipo: str
│   ├── combustivel: float
│   ├── massa: int
│   ├── prioridade: int
│   ├── criticidade: int
│   ├── chegada_orbita: int
│   ├── descricao: str
│   └── pousado: bool
│
└── Métodos
    ├── __init__()
    ├── __repr__()
    ├── is_combustivel_critico()
    └── is_em_emergencia()
```

#### Implementação

**Arquivo:** `src/structures/modulo.py`

```python
class Modulo:
    """Representa um módulo espacial."""
    
    def __init__(self, id_nome, tipo, prioridade, combustivel, 
                 massa, criticidade, chegada_orbita, descricao=""):
        """Construtor - inicializa atributos."""
        self.id_nome = id_nome
        self.tipo = tipo
        self.prioridade = prioridade
        self.combustivel = combustivel
        self.massa = massa
        self.criticidade = criticidade
        self.chegada_orbita = chegada_orbita
        self.descricao = descricao
        self.pousado = False
    
    def is_combustivel_critico(self, limite=25):
        """Verifica se combustível está crítico."""
        return self.combustivel <= limite
    
    def is_em_emergencia(self):
        """Verifica se módulo está em emergência."""
        return (self.is_combustivel_critico() or 
                self.criticidade <= 2)
```

#### Vantagens da Modelagem em Classe

| Vantagem | Benefício |
|----------|-----------|
| **Encapsulamento** | Dados e métodos relacionados agrupados |
| **Reutilização** | Criar múltiplos módulos sem duplicação |
| **Manutenibilidade** | Mudanças em um lugar afetam toda instância |
| **Semanticidade** | Código reflete conceito real (módulo espacial) |

#### Instanciação

```python
# Criar um módulo médico
med = Modulo(
    id_nome="MED-01",
    tipo="medico",
    prioridade=1,
    combustivel=25,
    massa=4500,
    criticidade=5,
    chegada_orbita=180,
    descricao="Módulo de suporte médico"
)

# Usar métodos
if med.is_combustivel_critico():
    print("ALERTA: Combustível crítico!")

# Acessar atributos
print(f"{med.id_nome}: {med.descricao}")
```

---

## COMPARAÇÃO COM PILHAS

### Pilha (Stack) vs Fila (Queue)

Uma **Pilha** funciona com princípio LIFO (Last In, First Out), ao contrário da fila.

```
FILA (FIFO):                    PILHA (LIFO):
Inserção: Fim                   Inserção: Topo
Remoção: Início                 Remoção: Topo

┌────────┐                      ┌────────┐
│ MED-01 │ ← Sai primeiro       │ MED-01 │ ← Sai último
├────────┤                      ├────────┤
│ ENG-02 │                      │ ENG-02 │
├────────┤                      ├────────┤
│ HAB-03 │ ← Entra primeiro     │ HAB-03 │ ← Sai primeiro
└────────┘                      └────────┘
```

### Por que não usar Pilha no MGPEB?

| Critério | Fila | Pilha |
|----------|------|-------|
| **Ordem de Processamento** | Justa (FIFO) | Inversa (LIFO) |
| **Previsibilidade** | Alta | Baixa |
| **Modelo Real** | ✓ Fila de espera | ✗ Não modela bem |
| **Justiça** | ✓ Modelos chegam na ordem | ✗ Último a chegar sai primeiro |

**Conclusão:** A Fila (FIFO) é mais apropriada para gerenciar justiça e ordem previsível de pouso.

---

## ANÁLISE DE COMPLEXIDADE

### Operações Principais

```
FILA FIFO (Usando List.pop(0)):
┌─────────────────────────────────────────┐
│ Operação        │ Complexidade │ Nota    │
├─────────────────────────────────────────┤
│ pop(0)          │ O(n)         │ Caro!   │
│ append()        │ O(1)         │ Rápido  │
│ len()           │ O(1)         │ Rápido  │
│ access [i]      │ O(1)         │ Rápido  │
└─────────────────────────────────────────┘

LISTA SIMPLES:
┌─────────────────────────────────────────┐
│ Operação        │ Complexidade │ Nota    │
├─────────────────────────────────────────┤
│ append()        │ O(1)         │ Rápido  │
│ access [i]      │ O(1)         │ Rápido  │
│ busca linear    │ O(n)         │ Médio   │
│ remoção final   │ O(1)         │ Rápido  │
└─────────────────────────────────────────┘

ALGORITMOS:
┌─────────────────────────────────────────┐
│ Algoritmo              │ Complexidade    │
├─────────────────────────────────────────┤
│ Bubble Sort            │ O(n²)           │
│ Busca Linear           │ O(n)            │
│ Processar FIFO (n=5)   │ O(5*n) = O(n)   │
└─────────────────────────────────────────┘
```

### Por que O(n²) no Bubble Sort está OK?

```
Número de elementos: 5
Comparações: (5-1) + (5-2) + (5-3) + (5-4) = 10

Bubble Sort O(5²) = 25 operações no pior caso
Quicksort O(5 log 5) = 25 operações no pior caso

Para 5 elementos: Praticamente idêntico!

Vantagem do Bubble Sort:
- Completamente previsível (sem casos patológicos)
- Fácil de entender e debugar
- Deterministicamente seguro
```

---

## DIAGRAMA DE FLUXO

### Fluxo Completo de Dados

```
ENTRADA
  │
  ├─→ MODULOS[5] (Lista de dados)
  │
  ├─→ fila_aproximacao = list(MODULOS)
  │        (Cria cópia para processamento FIFO)
  │
  ├─→ ordenar_por_prioridade(fila)
  │        (Bubble Sort O(n²))
  │
  └─→ PROCESSAMENTO FIFO
       │
       ├─→ WHILE len(fila) > 0:
       │     │
       │     ├─→ modulo = fila.pop(0)  [O(n)]
       │     │     (Remove primeiro)
       │     │
       │     ├─→ verificar_seguranca()
       │     │     (Lógica AND das 3 condições)
       │     │
       │     └─→ IF autorizado:
       │           └─→ lista_pousados.append()
       │         ELSE:
       │           └─→ lista_espera.append()
       │
       ├─→ buscar_menor_combustivel(lista_espera)
       │        (Busca Linear O(n))
       │
       └─→ gerar_relatorio_seguranca()
            (Exibe resultados)

SAÍDA
  ├─→ lista_pousados
  ├─→ lista_espera
  └─→ modulo_critico (ou None)
```

### Árvore de Chamadas

```
executar_simulacao()
├── ordenar_por_prioridade()           [O(n²)]
│   └── Bubble Sort
│
├── WHILE loop (5 iterações)
│   ├── fila.pop(0)                    [O(n)]
│   ├── verificar_pista()              [O(1)]
│   ├── verificar_seguranca()          [O(1)]
│   └── append() a lista              [O(1)]
│
├── buscar_menor_combustivel()         [O(n)]
│   └── Loop com comparação
│
└── gerar_relatorio_seguranca()        [O(n)]
    └── Iteração sobre listas
```

---

## EXEMPLOS PRÁTICOS

### Exemplo 1: Processamento FIFO Passo a Passo

```python
# Estado Inicial
fila_aproximacao = [MED-01, ENG-02, HAB-03, LOG-04, LAB-05]
lista_pousados = []
lista_espera = []

# Iteração 1: Processa MED-01
modulo = fila_aproximacao.pop(0)  # Remove MED-01
# fila_aproximacao = [ENG-02, HAB-03, LOG-04, LAB-05]

if verificar_seguranca(MED-01, 50, True):  # Suponha que retorna True
    lista_pousados.append(MED-01)
# lista_pousados = [MED-01]

# Iteração 2: Processa ENG-02
modulo = fila_aproximacao.pop(0)  # Remove ENG-02
# fila_aproximacao = [HAB-03, LOG-04, LAB-05]

if verificar_seguranca(ENG-02, 50, False):  # Suponha que retorna False
    lista_espera.append(ENG-02)
# lista_espera = [ENG-02]

# ... (iterações 3, 4, 5)

# Final
# lista_pousados = [MED-01, HAB-03, LAB-05]
# lista_espera = [ENG-02, LOG-04]
```

### Exemplo 2: Busca de Emergência (O(n))

```python
lista_espera = [ENG-02(40%), LOG-04(12%), HAB-03(30%)]

# Busca Linear
modulo_critico = lista_espera[0]  # ENG-02

for modulo in lista_espera:
    if modulo.combustivel < modulo_critico.combustivel:
        modulo_critico = modulo

# Iteração 1: LOG-04(12%) < ENG-02(40%) → modulo_critico = LOG-04
# Iteração 2: HAB-03(30%) > LOG-04(12%) → sem mudança

# Resultado: modulo_critico = LOG-04 ✓
```

### Exemplo 3: Bubble Sort Ordenação

```python
fila = [
    HAB-03 (prioridade=3),
    LAB-05 (prioridade=5),
    MED-01 (prioridade=1),
    ENG-02 (prioridade=2),
    LOG-04 (prioridade=4)
]

# Bubble Sort

# Passada 1:
# HAB-03(3) > LAB-05(5)? Não
# LAB-05(5) > MED-01(1)? Sim → Troca
# MED-01(1) > ENG-02(2)? Não
# ENG-02(2) > LOG-04(4)? Não
# Resultado: [HAB-03, MED-01, LAB-05, ENG-02, LOG-04]

# Passada 2:
# HAB-03(3) > MED-01(1)? Sim → Troca
# MED-01(1) > LAB-05(5)? Não
# LAB-05(5) > ENG-02(2)? Sim → Troca
# ENG-02(2) > LOG-04(4)? Não
# Resultado: [MED-01, HAB-03, ENG-02, LAB-05, LOG-04]

# ... (continua até completar ordenação)

# Final: [MED-01(1), ENG-02(2), HAB-03(3), LOG-04(4), LAB-05(5)] ✓
```

---

## RESUMO DAS ESTRUTURAS

| Estrutura | Uso | Complexidade | Exemplo |
|-----------|-----|--------------|---------|
| **Fila FIFO** | Processar módulos em ordem | pop(0)=O(n), append=O(1) | `fila_aproximacao` |
| **Lista** | Armazenar resultados | append=O(1), acesso=O(1) | `lista_pousados`, `lista_espera` |
| **Classe** | Representar módulo | N/A | `Modulo(id, tipo, ...)` |
| **Bubble Sort** | Ordenar por prioridade | O(n²) | `ordenar_por_prioridade()` |
| **Busca Linear** | Encontrar emergência | O(n) | `buscar_menor_combustivel()` |

---

## CONCLUSÕES

1. **Adequação:** Estruturas escolhidas refletem requisitos de segurança e previsibilidade
2. **Simplicidade:** Sem estruturas complexas - fácil validação
3. **Transparência:** Cada operação tem complexidade conhecida e previsível
4. **Escalabilidade:** Para 5 módulos (atual), complexidade é negligenciável
5. **Robustez:** Zero dependências externas garante funcionamento em ambiente embarcado

---

**Fim do Anexo - Estruturas de Dados MGPEB**
