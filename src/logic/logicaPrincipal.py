A = combustivel = 25
B = areaDePouso = True
C = criticidade = 4
D = massaDaNave = 90000


# Tabela de Verificação de segurança
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

# Sistema de autoização do Pouso de acordo com os parâmetros fornecidos
if A >= 50 and B == True and D >= 90000 and C > 3:
    print("\nPouso AUTORIZADO!")
elif (A >= 25 or C == 3 or D < 90000) and B == True:
    print("\nPouso AUTORIZADO com RISCO!")
    if A >= 25:
        print(f"Combustivel da Nave: {A}%")
    elif C == 3:
        print(f"Criticidade da Nave: {C}")
else:
    print("\nMissão Abortada!")
    print("Pouso NÃO AUTORIZADO!")
