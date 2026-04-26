"""
Banco de Dados de Módulos Espaciais - Missão Aurora Siger MGPEB
Responsável por: Victor (Modelagem do Cenário e Estruturas de Dados)

Contém a definição oficial dos 5 módulos que comporão a missão de colonização marciana.

Estruturado por: Victor G. Mantovani
Última atualização: 2026-04-26
"""

import sys
from pathlib import Path

# Adiciona o diretório src ao path para importações
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from structures.modulo import Modulo


# ============================================================================
# DEFINIÇÃO DOS 5 MÓDULOS PRINCIPAIS - Ordenados por Prioridade Crítica
# ============================================================================

MODULOS = [
    Modulo(
        id_nome="MED-01",
        tipo="medico",
        prioridade=1,
        combustivel=25,
        massa=4500,
        criticidade=5,
        chegada_orbita=180,
        descricao="Módulo de suporte médico com equipamentos de diagnóstico avançado, "
                  "farmácia e centro cirúrgico para emergências. Essencial para sobrevivência da tripulação."
    ),
    
    Modulo(
        id_nome="ENG-02",
        tipo="energia",
        prioridade=2,
        combustivel=40,
        massa=8000,
        criticidade=5,
        chegada_orbita=150,
        descricao="Unidade de geração e distribuição de energia. Inclui painéis solares, "
                  "baterias de backup e sistema de roteamento de potência. Estrutura: 1.5t, "
                  "Sistemas: 0.5t, Baterias: 6t."
    ),
    
    Modulo(
        id_nome="HAB-03",
        tipo="habitacao",
        prioridade=3,
        combustivel=30,
        massa=12000,
        criticidade=4,
        chegada_orbita=200,
        descricao="Módulo pressurizado para habitação da tripulação com sistema de suporte à vida "
                  "integrado. Estrutura pressurizada 9t, sistema de suporte 5t, mobiliário 4t, "
                  "água armazenada 4t."
    ),
    
    Modulo(
        id_nome="LOG-04",
        tipo="logistico",
        prioridade=4,
        combustivel=12,
        massa=15000,
        criticidade=2,
        chegada_orbita=120,
        descricao="Módulo de logística com rovers para exploração de superfície. Contém "
                  "equipamento de escavação, armazenamento de suprimentos e sistema de "
                  "transporte. COMBUSTÍVEL CRÍTICO - RISCO DE FALHA!"
    ),
    
    Modulo(
        id_nome="LAB-05",
        tipo="laboratorial",
        prioridade=5,
        combustivel=50,
        massa=6000,
        criticidade=1,
        chegada_orbita=90,
        descricao="Laboratório pressurizável para experimentos científicos e pesquisa de "
                  "sustentabilidade. Inclui sistema hidropônico para produção alimentar, "
                  "iluminação LED agrícola e equipamentos analíticos."
    ),
]


# ============================================================================
# FUNÇÕES UTILITÁRIAS
# ============================================================================

def obter_modulo_por_id(id_nome):
    """Retorna um módulo específico pelo ID."""
    for modulo in MODULOS:
        if modulo.id_nome == id_nome:
            return modulo
    return None


def obter_modulos_por_tipo(tipo):
    """Retorna todos os módulos de um tipo específico."""
    return [m for m in MODULOS if m.tipo == tipo]


def obter_modulos_criticos():
    """Retorna módulos em estado crítico (combustível baixo ou alta criticidade)."""
    return [m for m in MODULOS if m.is_em_emergencia()]


def listar_modulos():
    """Exibe lista formatada de todos os módulos."""
    print("\n" + "=" * 80)
    print("📦 MÓDULOS ESPACIAIS - MISSÃO AURORA SIGER".center(80))
    print("=" * 80)
    for i, modulo in enumerate(MODULOS, 1):
        print(f"\n{i}. {modulo.id_nome} ({modulo.tipo.upper()})")
        print(f"   └─ Prioridade: {modulo.prioridade} | Criticidade: {modulo.criticidade}")
        print(f"   └─ Combustível: {modulo.combustivel}% | Massa: {modulo.massa}kg")
        print(f"   └─ Chegada à órbita: {modulo.chegada_orbita} min")
        print(f"   └─ {modulo.descricao}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Teste básico
    listar_modulos()
    
    print("\n📊 MÓDULOS EM ESTADO CRÍTICO:")
    for modulo in obter_modulos_criticos():
        print(f"  ⚠️  {modulo.id_nome} - Combustível: {modulo.combustivel}%")
