# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o == , que é um operador lógico que questiona se um valor é igual a outro

print(10 == 10)  # True, porque 10 é igual a 10
print(10 == 5)   # False, porque 10 não é igual a 5
print(3.14 == 3.14)  # True, porque 3.14 é igual a 3.14
print(3.14 == -3.14)  # False, porque 3.14 não é igual a -3.14
print('Hello' == 'Hello')  # True, porque as strings são iguais
print('Hello' == 'hello')  # False, porque as strings são diferentes (case-sensitive)
print(True == True)  # True, porque ambos são True

print(type(10 == 10))  # <class 'bool'>, o resultado é do tipo boolean, porque o tipo será sobre o resultado retornado, e não sobre os valores comparados
print(type(10 == 5))   # <class 'bool'>, o resultado é  do tipo boolean