"""
Tipos int e float
Int: números inteiros, sem parte decimal. Ex: 1, 2, 3, -10, 0 - Primitivos
Float: números com parte decimal. Ex: 1.5, -0.75, 3.14 (flutante)
"""
# Exemplos de números inteiros (int)
print(10)  # int
print(-5)  # int
print(0)   # int

# Exemplos de números de ponto flutuante (float), sempre utilizar o . para indicar casas decimais
print(3.14)  # float
print(-0.75, 0.75) # float
print(2.0)   # float (mesmo que 2, mas com parte decimal)

# A classe type() pode ser usada para verificar o tipo de um valor
print(type('Hello World'))        # str (string)
print(type(10), type(-19))        # int (inteiro)
print(type(3.20), type(-3.20))    # float (ponto flutuante)
print(type(True), type(False))    # bool (booleans)
print(type(None))                 # NoneType (tipo de valor nulo)
print(type([1, 2, 3]))            # list (uma coleção ordenada e mutável de itens)
print(type((1, 2, 3)))            # tuple (coleção ordenada e imutável de itens)
print(type({'key': 'value'}))     # dict (dicionário, que é uma coleção de pares chave-valor)
print(type({1, 2, 3}))            # set (conjunto, que é coleção desordenada e única de itens)