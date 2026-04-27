"""
Módulo de Estrutura de Dados - Classe Modulo
Responsável por: Victor (Modelagem do Cenário e Estruturas de Dados)

Componente central para representar módulos espaciais da Missão Aurora Siger.
Define a estrutura base e comportamentos de cada carga útil.
"""


class Modulo:
    """
    Classe que representa um módulo espacial com seus atributos críticos.
    
    Attributes:
        id_nome (str): Identificador único do módulo (ex: MED-01, ENG-02)
        tipo (str): Função do módulo (medico, energia, habitacao, logistico, laboratorial)
        prioridade (int): Prioridade de pouso (1 = máxima prioridade)
        combustivel (float): Nível de combustível em porcentagem (0-100)
        massa (int): Peso total do módulo em kg
        criticidade (int): Nível de importância de 1 a 5 (5 = insubstituível)
        chegada_orbita (int): Tempo estimado até órbita marciana em minutos
        descricao (str): Resumo da função e conteúdo do módulo
        pousado (bool): Flag indicando se o módulo já pousou
    """
    
    def __init__(self, id_nome, tipo, prioridade, combustivel, massa, criticidade, 
                 chegada_orbita, descricao=""):
        """
        Inicializa um novo módulo espacial.
        
        Args:
            id_nome (str): Identificador único
            tipo (str): Tipo de módulo
            prioridade (int): Ordem de prioridade de pouso
            combustivel (float): Percentual de combustível (0-100)
            massa (int): Massa em kg
            criticidade (int): Nível de criticidade (1-5)
            chegada_orbita (int): Tempo em minutos até órbita
            descricao (str): Descrição do módulo (opcional)
        """
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
        return f"Modulo({self.id_nome} - {self.tipo.upper()} | Comb: {self.combustivel}% | {status})"
    
    def is_combustivel_critico(self, limite=25):
        """Verifica se combustível está em nível crítico."""
        return self.combustivel <= limite
    
    def is_em_emergencia(self):
        """Verifica se o módulo está em estado de emergência."""
        return self.is_combustivel_critico() or self.criticidade <= 2
