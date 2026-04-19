# 🚀 Missão Aurora Siger: Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg)]()
[![Instituição](https://img.shields.io/badge/Instituição-FIAP-ed145b.svg)]()

> **Sistema embarcado de simulação logística e aproximação orbital para a colonização marciana.**

## 📋 Sobre o Projeto

O **MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base)** é um projeto acadêmico de Ciência da Computação desenvolvido para gerenciar a descida segura de cargas úteis na superfície de Marte durante a missão "Aurora Siger". 

Devido às severas restrições de hardware simuladas (ambiente de alta radiação cósmica semelhante ao *Apollo Guidance Computer*), o sistema foi projetado com **código Python puro**, utilizando estruturas de dados lineares estritas (Filas FIFO) e algoritmos clássicos de ordenação e busca, garantindo previsibilidade de tempo de execução ($O(n^2)$ máximo) e baixo custo computacional.

## 🛠️ Arquitetura e Tecnologias

* **Linguagem:** Python 3
* **Estrutura de Dados Principal:** Fila (Queue) modelada via listas nativas (`pop(0)`, `append`).
* **Algoritmo de Ordenação:** *Bubble Sort* (implementação nativa manual para reordenar prioridades).
* **Algoritmo de Busca:** *Busca Linear* (para identificação de módulos em estado crítico).
* **Dependências:** Nenhuma biblioteca externa necessária (apenas os módulos nativos `random` e `time`).

## 📦 Especificações da Carga Útil (Payload)

A missão é composta por 5 módulos vitais, ordenados por prioridade de sobrevivência e criticidade operacional. A alocação reflete princípios éticos e **Sociais (S)** do ESG, priorizando o suporte à vida humano em caso de contingências.

| ID do Módulo | Função | Prioridade | Massa (kg) | Combustível Inicial | Criticidade |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **MED-01** | Suporte Médico | 1 | 4.500 | 25% | Extrema |
| **ENG-02** | Geração de Energia | 2 | 8.000 | 40% | Alta |
| **HAB-03** | Habitação/Abrigo | 3 | 12.000 | 30% | Alta |
| **LOG-04** | Logística/Rovers | 4 | 15.000 | 12% | Média |
| **LAB-05** | Pesquisa Científica | 5 | 6.000 | 50% | Baixa |

## 🧠 Lógica de Decisão e Segurança

A autorização de pouso é governada por um processador de fluxo rígido baseado em portas lógicas booleanas (`AND`). O pouso ($A$) só é deferido se as três variáveis de ambiente forem verdadeiras:

$$A = C \land W \land P$$

1. **C (Combustível):** Nível de combustível da sonda $> 10\%$.
2. **W (Clima):** Velocidade do vento marciano $< 80 \text{ km/h}$.
3. **P (Pista):** Varredura de radar orbital detecta pista de pouso desobstruída (`True`).

Módulos negados são alocados em uma `lista_espera` para reavaliação ou resgate de emergência.

## 🚀 Como Executar a Simulação

1. Clone o repositório para o seu ambiente local:
   ```cmd
   git clone [https://github.com/DevLounge-FIAP/mars-landing-management-system.git](https://github.com/DevLounge-FIAP/mars-landing-management-system.git)
