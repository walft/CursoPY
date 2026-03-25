"""
Flag (bandeira) - Marcar um local
Nome = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

condicao = False
passou_if = None

if condicao:
    print('Faça algo')
    passou_if = True
else:
    print('Não faça algo')

print(passou_if, passou_if is None)
print(passou_if, passou_if is not None)