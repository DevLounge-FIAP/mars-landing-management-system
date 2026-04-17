combustivel = 70
areaDePouso = True
criticidade = 4
massaDaNave = 21000


# Tabela de Verificação de segurança
print("=-=-=-=-=- VERIFICAÇÃO DE SEGURANÇA =-=-=-=-=-")
if combustivel < 25:
    print(f"{'Combustível':<25} | {combustivel:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Combustível':<25} | {combustivel:^10} | {'OK!':^10}")
if areaDePouso != True:
    print(f"{'Local de Pouso':<25} | {areaDePouso:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Local de Pouso':<25} | {areaDePouso:^10} | {'OK!':^10}")
if criticidade < 4:
    print(f"{'Criticidade da Nave':<25} | {criticidade:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Criticidade da Nave':<25} | {criticidade:^10} | {'OK!':^10}")
if massaDaNave:
    print(f"{'Massa da Nave':<25} | {massaDaNave:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Massa da Nave':<25} | {massaDaNave:^10} | {'OK!':^10}")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Sistema de autoização do Pouso de acordo com os parâmetros fornecidos
if combustivel >= 25 and areaDePouso == True:
    print("\nPouso AUTORIZADO!")
else:
    print("\nPouso NÃO AUTORIZADO!")
