combustivel = 70
localDePouso = True
vento = 20
integridadeDosMotores = True
sensores = 90

# Tabela de Verificação de segurança
print("=-=-=-=-=- VERIFICAÇÃO DE SEGURANÇA =-=-=-=-=-")
if combustivel < 60:
    print(f"{'Combustível':<25} | {combustivel:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Combustível':<25} | {combustivel:^10} | {'OK!':^10}")
if localDePouso != True:
    print(f"{'Local de Pouso':<25} | {localDePouso:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Local de Pouso':<25} | {localDePouso:^10} | {'OK!':^10}")
if integridadeDosMotores != True:
    print(f"{'Integridade dos Motores':<25} | {integridadeDosMotores:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Integridade dos Motores':<25} | {integridadeDosMotores:^10} | {'OK!':^10}")
if sensores < 70:
    print(f"{'Senssores':<25} | {sensores:^10} | {'ALERTA!':^10}")
else:
    print(f"{'Senssores':<25} | {sensores:^10} | {'OK!':^10}")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Sistema de autoização do Pouso de acordo com os parâmetros fornecidos
if combustivel >= 60 and localDePouso == True and vento <= 30 and integridadeDosMotores == True and sensores >= 70:
    print("\nPouso AUTORIZADO!")
else:
    print("\nPouso NÃO AUTORIZADO!")
