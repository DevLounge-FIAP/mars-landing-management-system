"""
Pacote de Lógica de Operação
Contém algoritmos e processos para gerenciamento de pouso.

Responsável por: Bruno (Lógica de Decisão e Portas Lógicas)

Módulos:
    - logica_pouso.py: Lógica de decisão, portas lógicas AND, algoritmos de busca e ordenação
"""

from .logica_pouso import (
    verificar_pista,
    verificar_seguranca,
    buscar_menor_combustivel,
    ordenar_por_prioridade,
    gerar_relatorio_seguranca
)

__all__ = [
    'verificar_pista',
    'verificar_seguranca',
    'buscar_menor_combustivel',
    'ordenar_por_prioridade',
    'gerar_relatorio_seguranca'
]
