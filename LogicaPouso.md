# 🚀 Simulação de Pouso em Marte — Sistema de Portas Lógicas

<div align="center">

![Mars](https://img.shields.io/badge/Destino-Marte%20🔴-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

> **Módulo de Decisão de Pouso** — Sistema baseado em lógica booleana para autorizar ou bloquear o pouso de um módulo espacial em Marte.

</div>

---

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Variáveis do Sistema](#-variáveis-do-sistema)
- [Regras de Decisão Booleana](#-regras-de-decisão-booleana)
- [Diagrama de Portas Lógicas](#-diagrama-de-portas-lógicas)
- [Código Python](#-código-python)
- [Saída Esperada](#-saída-esperada)

---

## 🛸 Sobre o Projeto

Este módulo é responsável por **definir e representar as regras de decisão de pouso** usando portas lógicas. O sistema analisa quatro variáveis críticas da nave e, com base em expressões booleanas, determina se o pouso será:

| Resultado | Condição |
|-----------|----------|
| ✅ **AUTORIZADO** | Todos os parâmetros estão no limite ideal |
| ⚠️ **AUTORIZADO COM RISCO** | Parâmetros parcialmente fora do ideal |
| ❌ **MISSÃO ABORTADA** | Condições críticas impedem o pouso seguro |

---

## 📊 Variáveis do Sistema

| Variável | Identificador | Tipo | Descrição |
|----------|--------------|------|-----------|
| Combustível | `A` | `int` (%) | Nível de combustível restante na nave |
| Área de Pouso | `B` | `bool` | Disponibilidade da área de pouso |
| Criticidade | `C` | `int` (1–5) | Nível de criticidade dos sensores da nave |
| Massa da Nave | `D` | `int` (Kg) | Massa total do módulo de pouso |

### 🔍 Limites Críticos por Variável

```
Combustível (A):
  A < 25%        →  🔴 CRÍTICO
  25% ≤ A < 50%  →  🟡 ALERTA
  A ≥ 50%        →  🟢 OK

Área de Pouso (B):
  B = False      →  🔴 CRÍTICO
  B = True       →  🟢 OK

Criticidade (C):
  C < 3          →  🔴 CRÍTICO
  C = 3          →  🟡 ALERTA
  C > 3          →  🟢 OK

Massa da Nave (D):
  D < 70.000 Kg  →  🔴 CRÍTICO
  70.000 ≤ D < 90.000 Kg  →  🟡 ALERTA
  D ≥ 90.000 Kg  →  🟢 OK
```

---

## 🔣 Regras de Decisão Booleana

As condições de pouso são traduzidas em expressões booleanas da seguinte forma:

### Definição das Proposições

```
P₁ = (A ≥ 50)      → Combustível suficiente
P₂ = (B = True)    → Área de pouso disponível
P₃ = (C > 3)       → Criticidade aceitável
P₄ = (D ≥ 90.000)  → Massa dentro do limite ideal

P₅ = (A ≥ 25)      → Combustível mínimo
P₆ = (C = 3)       → Criticidade no limite
P₇ = (D < 90.000)  → Massa abaixo do ideal
```

### Expressões Booleanas

**✅ Pouso AUTORIZADO:**
```
AUTORIZADO = P₁ AND P₂ AND P₃ AND P₄
           = (A ≥ 50) AND (B = True) AND (C > 3) AND (D ≥ 90.000)
```

**⚠️ Pouso AUTORIZADO COM RISCO:**
```
RISCO = (P₅ OR P₆ OR P₇) AND P₂
      = ((A ≥ 25) OR (C = 3) OR (D < 90.000)) AND (B = True)
      E NOT AUTORIZADO
```

**❌ Missão ABORTADA (pouso BLOQUEADO):**
```
BLOQUEADO = NOT (AUTORIZADO OR RISCO)
          = NOT P₂  (área indisponível é condição absoluta de bloqueio)
          OR (NOT P₅ AND NOT P₆)  (combustível e criticidade ambos críticos)
```

---

## 🔌 Diagrama de Portas Lógicas

Os diagramas abaixo representam visualmente como o sistema combina os sinais de entrada para produzir a decisão de pouso. Cada cenário possui sua própria combinação de portas **AND**, **OR** e **NOT**.

---

### ✅ Diagrama — Pouso AUTORIZADO (condição ideal)

> Todas as entradas devem satisfazer seus limites ideais. Duas portas **AND** em série garantem que **A**, **B**, **C** e **D** estejam todos no nível OK.
> 
> **Expressão:** `(A · B) · (C · D)`

![Diagrama Pouso Autorizado](diagrama_autorizado.png)

---

### ⚠️ Diagrama — Pouso com Alerta (condição parcial)

> Pelo menos uma variável está fora do ideal, mas a área de pouso está disponível. Uma porta **OR** agrupa as condições de alerta e uma porta **AND** verifica a disponibilidade da área.
> 
> **Expressão:** `(A + C + D) · B`

![Diagrama Pouso com Alerta](diagrama_risco.png)

---

### ❌ Diagrama — Missão Abortada (bloqueio de pouso)

> Parâmetros críticos detectados. A porta **NOT** na entrada **B** representa a ausência ou bloqueio da área de pouso, combinada com os demais alertas via **OR**.
> 
> **Expressão:** `(A + C + D + NOT B)`

![Diagrama Missão Abortada](diagrama_abortado.png)

---

## 💻 Código Python

```python
# =============================================
# SISTEMA DE VERIFICAÇÃO DE POUSO EM MARTE
# Módulo: Portas Lógicas e Expressões Booleanas
# =============================================

# --- Variáveis de entrada ---
A = 25          # Combustível (%)
B = True        # Área de Pouso (True/False)
C = 4           # Criticidade (1–5)
D = 90000       # Massa da Nave (Kg)

# --- Tabela de Verificação de Segurança ---
print("=-=-=-=-=- VERIFICAÇÃO DE SEGURANÇA GERAL DOS MÓDULOS =-=-=-=-=-")

if A < 25:
    print(f"{'Combustível':<25} | {f'{A} %':^10} | {'CRÍTICO!':^10}")
elif A < 50:
    print(f"{'Combustível':<25} | {f'{A} %':^10} | {'ALERTA!':^10}")
else:
    print(f"{'Combustível':<25} | {f'{A} %':^10} | {'OK!':^10}")

if B != True:
    print(f"{'Local de Pouso':<25} | {B:^10} | {'CRÍTICO!':^10}")
else:
    print(f"{'Local de Pouso':<25} | {B:^10} | {'OK!':^10}")

if C < 3:
    print(f"{'Criticidade da Nave':<25} | {C:^10} | {'CRÍTICO!':^10}")
elif C == 3:
    print(f"{'Criticidade da Nave':<25} | {C:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Criticidade da Nave':<25} | {C:^10} | {'OK!':^10}")

if D < 70000:
    print(f"{'Massa da Nave':<25} | {f'{D} Kg':^10} | {'CRÍTICO!':^10}")
elif D < 90000:
    print(f"{'Massa da Nave':<25} | {f'{D} Kg':^10} | {'ALERTA!':^10}")
else:
    print(f"{'Massa da Nave':<25} | {f'{D} Kg':^10} | {'OK!':^10}")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# --- Sistema de Autorização do Pouso ---
# Expressão: AUTORIZADO = (A≥50) AND (B=True) AND (D≥90000) AND (C>3)
if A >= 50 and B == True and D >= 90000 and C > 3:
    print("\nPouso AUTORIZADO!")

# Expressão: RISCO = ((A≥25) OR (C=3) OR (D<90000)) AND (B=True)
elif (A >= 25 or C == 3 or D < 90000) and B == True:
    print("\nPouso AUTORIZADO com RISCO!")
    if A >= 25:
        print(f"Combustivel da Nave: {A}%")
    elif C == 3:
        print(f"Criticidade da Nave: {C}")

# Expressão: ABORTADO = NOT(AUTORIZADO OR RISCO)
else:
    print("\nMissão Abortada!")
    print("Pouso NÃO AUTORIZADO!")
```

---

## 🖥️ Saída Esperada

Com os valores padrão (`A=25`, `B=True`, `C=4`, `D=90000`):

```
=-=-=-=-=- VERIFICAÇÃO DE SEGURANÇA GERAL DOS MÓDULOS =-=-=-=-=-
Combustível               |   25 %    |   ALERTA!  
Local de Pouso            |   True    |    OK!     
Criticidade da Nave       |     4     |    OK!     
Massa da Nave             | 90000 Kg  |    OK!     
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Pouso AUTORIZADO com RISCO!
Combustivel da Nave: 25%
```

### Tabela de Casos de Teste

| A (%) | B | C | D (Kg) | Resultado Esperado |
|-------|---|---|--------|-------------------|
| 60 | True | 4 | 95000 | ✅ Pouso Autorizado |
| 30 | True | 4 | 85000 | ⚠️ Autorizado com Risco |
| 25 | True | 4 | 90000 | ⚠️ Autorizado com Risco |
| 10 | False | 2 | 60000 | ❌ Missão Abortada |
| 50 | False | 5 | 95000 | ❌ Missão Abortada |

---
