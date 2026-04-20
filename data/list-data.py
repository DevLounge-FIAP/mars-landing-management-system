modulo_habitacao = {
    "id": "MOD-01",
    "tipo": "habitacao",
    "combustivel": 0.74,
    "massa": 24000,  #Estrutura pressurizada 9t, sistema de suporte à vida 5 t, mobiliário + racks internos 4t, água armazenada 4t, parte elétrica 2t
    "criticidade": 1,
    "chegada_orbita": 180,  # em minutos
    "descrição": "Módulo pressurizado para habitação da tripulação com suporte à vida integrado."
}

modulo_energia = {
    "id": "MOD-02",
    "tipo": "energia",
    "combustivel": 0.63,
    "massa":99000,  # Estrutura pressurizada 9t, tanques estruturais 6t, isolamento térmico 3t, controle e sensores 1t, propelente líquido (LOX + Metano) 80t
    "criticidade": 2,
    "chegada_orbita": 150,  # em minutos
    "descrição": "Unidade dedicada ao armazenamento de propelente e alimentação do sistema de propulsão principal e auxiliar da nave."
}

modulo_laboratorial = {
    "id": "MOD-03",
    "tipo": "laboratorial",
    "combustivel": 0.45,
    "massa": 25000,  #Estrutura pressurizada 10t, equipamentos científicos 5t, sistemas hidropônico 3t, Iluminação LED agrícola 2t, água armazenada 5t
    "criticidade": 3,
    "chegada_orbita": 120,  # em minutos
    "descrição": "Módulo pressurizado para realização de experimentos científicos, pesquisas voltadas a sustentabilidade da nave durante a missão e recursos alimentícios."
}

modulo_logistico = {
    "id": "MOD-04",
    "tipo": "logistico",
    "combustivel": 0.22,
    "massa": 20000,  #Estrutura pressurizada 8t, Comida 5t, peças sobressalentes 3t, equipamentos de manuseio 2t, água armazenada 2t
    "criticidade": 5,
    "chegada_orbita": 60,  # em minutos
    "descrição": "Módulo pressurizado para armazenamento de suprimentos, equipamentos e comida durante a missão."
}

modulo_medico = {
    "id": "MOD-05",
    "tipo": "medico",
    "combustivel": 0.39,
    "massa": 14500,  #Estrutura pressurizada 5t, equipamentos médicos 5t, medicamentos 500kg, sistemas de suporte à vida 2t, água armazenada 2t
    "criticidade": 4,
    "chegada_orbita": 90,  # em minutos
    "descrição": "Módulo pressurizado para atendimento médico e primeiros socorros durante a missão."
}

fila_de_pouso = [modulo_logistico, modulo_medico, modulo_laboratorial, modulo_energia, modulo_habitacao]

modulos_pousados = []

modulos_em_espera = []

modulos_em_alerta = []