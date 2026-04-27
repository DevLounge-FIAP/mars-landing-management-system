"""
Suite de Testes para Sistema MGPEB
Valida estruturas de dados, algoritmos de ordenação e lógica de segurança.

Responsável por: Aelton (Engenharia de Software)

Testa:
    ✓ Classe Modulo (Victor)
    ✓ Banco de dados de módulos (Victor)
    ✓ Algoritmos: Bubble Sort, Busca Linear (Bruno)
    ✓ Lógica de segurança: portas AND (Bruno)
"""

import sys
from pathlib import Path

# Adiciona caminho para importações
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.structures.modulo import Modulo
from data.modulos_dados import MODULOS, obter_modulo_por_id, obter_modulos_criticos
from src.logic import (
    ordenar_por_prioridade,
    buscar_menor_combustivel,
    verificar_seguranca
)


class TestModulo:
    """Testes para a classe Modulo."""
    
    def test_criacao_modulo(self):
        """Testa criação de instância de Modulo."""
        modulo = Modulo(
            id_nome="TEST-01",
            tipo="teste",
            prioridade=1,
            combustivel=50,
            massa=5000,
            criticidade=3,
            chegada_orbita=100,
            descricao="Módulo de teste"
        )
        assert modulo.id_nome == "TEST-01"
        assert modulo.combustivel == 50
        assert modulo.pousado == False
        print("[OK] test_criacao_modulo passou")
    
    def test_combustivel_critico(self):
        """Testa detecção de combustível crítico."""
        modulo_critico = Modulo("CRIT-01", "teste", 1, 20, 5000, 3, 100)
        modulo_ok = Modulo("OK-01", "teste", 1, 50, 5000, 3, 100)
        
        assert modulo_critico.is_combustivel_critico(25) == True
        assert modulo_ok.is_combustivel_critico(25) == False
        print("[OK] test_combustivel_critico passou")
    
    def test_em_emergencia(self):
        """Testa detecção de emergência."""
        modulo_emergencia = Modulo("EMG-01", "teste", 1, 50, 5000, 1, 100)
        modulo_normal = Modulo("NRM-01", "teste", 1, 50, 5000, 4, 100)
        
        assert modulo_emergencia.is_em_emergencia() == True  # Criticidade <= 2
        assert modulo_normal.is_em_emergencia() == False
        print("[OK] test_em_emergencia passou")
    
    def test_repr_modulo(self):
        """Testa representação em string."""
        modulo = Modulo("TST-01", "teste", 1, 50, 5000, 3, 100)
        representacao = repr(modulo)
        assert "TST-01" in representacao
        assert "teste" in representacao.lower()
        print("[OK] test_repr_modulo passou")


class TestModulosDados:
    """Testes para banco de dados de módulos."""
    
    def test_quantidade_modulos(self):
        """Verifica se existem exatamente 5 módulos."""
        assert len(MODULOS) == 5, f"Esperado 5 módulos, encontrado {len(MODULOS)}"
        print("[OK] test_quantidade_modulos passou")
    
    def test_ids_unicos(self):
        """Verifica se todos os IDs são únicos."""
        ids = [m.id_nome for m in MODULOS]
        assert len(ids) == len(set(ids)), "IDs duplicados encontrados"
        assert ids == ["MED-01", "ENG-02", "HAB-03", "LOG-04", "LAB-05"]
        print("[OK] test_ids_unicos passou")
    
    def test_prioridades_sequenciais(self):
        """Verifica se as prioridades são 1-5 sequencialmente."""
        prioridades = [m.prioridade for m in MODULOS]
        assert prioridades == [1, 2, 3, 4, 5]
        print("[OK] test_prioridades_sequenciais passou")
    
    def test_obter_modulo_por_id(self):
        """Testa função de busca por ID."""
        modulo = obter_modulo_por_id("MED-01")
        assert modulo is not None
        assert modulo.tipo == "medico"
        
        modulo_inexistente = obter_modulo_por_id("INEXISTENTE")
        assert modulo_inexistente is None
        print("[OK] test_obter_modulo_por_id passou")
    
    def test_modulos_criticos(self):
        """Verifica identificação de módulos críticos."""
        criticos = obter_modulos_criticos()
        # LOG-04 tem combustível crítico (12%)
        # MED-01 tem criticidade 5 (emergência)
        assert len(criticos) > 0
        ids_criticos = [m.id_nome for m in criticos]
        assert "LOG-04" in ids_criticos or "MED-01" in ids_criticos
        print("[OK] test_modulos_criticos passou")
    
    def test_atributos_obrigatorios(self):
        """Verifica se todos os módulos têm atributos essenciais."""
        for modulo in MODULOS:
            assert modulo.id_nome is not None
            assert modulo.tipo is not None
            assert 1 <= modulo.prioridade <= 5
            assert 0 <= modulo.combustivel <= 100
            assert modulo.massa > 0
            assert 1 <= modulo.criticidade <= 5
            assert modulo.chegada_orbita > 0
        print("[OK] test_atributos_obrigatorios passou")


class TestAlgoritmos:
    """Testes para algoritmos de ordenação e busca (Bruno)."""
    
    def test_bubble_sort(self):
        """Testa ordenação Bubble Sort."""
        # Cria fila fora de ordem
        fila_teste = [
            Modulo("T5", "teste", 5, 50, 5000, 3, 100),
            Modulo("T1", "teste", 1, 50, 5000, 3, 100),
            Modulo("T3", "teste", 3, 50, 5000, 3, 100),
        ]
        
        fila_ordenada = ordenar_por_prioridade(fila_teste)
        prioridades = [m.prioridade for m in fila_ordenada]
        assert prioridades == [1, 3, 5], f"Prioridades incorretas: {prioridades}"
        print("[OK] test_bubble_sort passou")
    
    def test_busca_linear(self):
        """Testa busca linear por menor combustível."""
        fila_teste = [
            Modulo("T1", "teste", 1, 50, 5000, 3, 100),
            Modulo("T2", "teste", 2, 20, 5000, 3, 100),
            Modulo("T3", "teste", 3, 70, 5000, 3, 100),
        ]
        
        critico = buscar_menor_combustivel(fila_teste)
        assert critico.id_nome == "T2"
        assert critico.combustivel == 20
        print("[OK] test_busca_linear passou")
    
    def test_busca_fila_vazia(self):
        """Testa busca com fila vazia."""
        critico = buscar_menor_combustivel([])
        assert critico is None
        print("[OK] test_busca_fila_vazia passou")


class TestLogicaSeguranca:
    """Testes para lógica de segurança (Portas AND - Bruno)."""
    
    def test_seguranca_autorizado(self):
        """Testa autorização quando todas as condições são OK."""
        modulo = Modulo("TEST-01", "teste", 1, 50, 5000, 3, 100)
        autorizado = verificar_seguranca(modulo, 50, True)
        assert autorizado == True
        print("[OK] test_seguranca_autorizado passou")
    
    def test_seguranca_combustivel_critico(self):
        """Testa rejeição com combustível crítico."""
        modulo = Modulo("TEST-02", "teste", 1, 5, 5000, 3, 100)
        autorizado = verificar_seguranca(modulo, 50, True)
        assert autorizado == False
        print("[OK] test_seguranca_combustivel_critico passou")
    
    def test_seguranca_pista_obstruida(self):
        """Testa rejeição com pista obstruída."""
        modulo = Modulo("TEST-03", "teste", 1, 50, 5000, 3, 100)
        autorizado = verificar_seguranca(modulo, 50, False)
        assert autorizado == False
        print("[OK] test_seguranca_pista_obstruida passou")
    
    def test_seguranca_vento_critico(self):
        """Testa rejeição com vento muito forte."""
        modulo = Modulo("TEST-04", "teste", 1, 50, 5000, 3, 100)
        autorizado = verificar_seguranca(modulo, 100, True)
        assert autorizado == False
        print("[OK] test_seguranca_vento_critico passou")


def executar_testes():
    """Executa todas as suites de testes."""
    print("\n" + "=" * 70)
    print("EXECUTANDO SUITE DE TESTES - SISTEMA MGPEB".center(70))
    print("=" * 70 + "\n")
    
    test_modulo = TestModulo()
    test_modulo.test_criacao_modulo()
    test_modulo.test_combustivel_critico()
    test_modulo.test_em_emergencia()
    test_modulo.test_repr_modulo()
    
    print()
    
    test_dados = TestModulosDados()
    test_dados.test_quantidade_modulos()
    test_dados.test_ids_unicos()
    test_dados.test_prioridades_sequenciais()
    test_dados.test_obter_modulo_por_id()
    test_dados.test_modulos_criticos()
    test_dados.test_atributos_obrigatorios()
    
    print()
    
    test_alg = TestAlgoritmos()
    test_alg.test_bubble_sort()
    test_alg.test_busca_linear()
    test_alg.test_busca_fila_vazia()
    
    print()
    
    test_seg = TestLogicaSeguranca()
    test_seg.test_seguranca_autorizado()
    test_seg.test_seguranca_combustivel_critico()
    test_seg.test_seguranca_pista_obstruida()
    test_seg.test_seguranca_vento_critico()
    
    print("\n" + "=" * 70)
    print("[OK] TODOS OS TESTES PASSARAM COM SUCESSO!".center(70))
    print("=" * 70 + "\n")


if __name__ == "__main__":
    executar_testes()
