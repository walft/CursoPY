# Introdução aos operadores aritméticos (matemática)
# + Adição
adicao = 10 + 5
print("Adição:", adicao)
# - Subtração
subtracao = 10 - 5
print("Subtração:", subtracao)
# * Multiplicação
multiplicacao = 10 * 5
print("Multiplicação:", multiplicacao)
# / Divisão
divisao = 10 / 5 # Sempre será um float.
print("Divisão:", divisao)
# // Divisão inteira
divisao_inteira = 10 // 2.2
print("Divisão inteira:", divisao_inteira) #Todo número após o ponto, não será considerado.
# % Módulo (resto da divisão)
modulo = 10 % 3
print("Módulo, resto da divisão:", modulo)
# ** Exponenciação
exponenciacao = 2 ** 3
print("Exponenciação:", exponenciacao)
# Ordem de precedência: (), **, *, /, //, %, +, -
resultado = 10 + 5 * 2 ** 3
print("Resultado da expressão:", resultado)

# Exemplo prático de como pode ser utilizado o resto de uma divisão (módulo) para verificar se um número é divisivel por outro.
numero = 16
divisor = 8
resto = numero % divisor
print(f"O resto da divisão de {numero} por {divisor} é: {resto}, a afirmação se {numero} é divisível por {divisor} é: {resto == 0}")

# Outro exemplo é verificar se o número é par ou ímpar utilizando o resto da divisão por 2.
numero2 = 15
resto2 = numero2 % 2
print(f"O resto da divisão de {numero2} por 2 é: {resto2}, a afirmação se {numero2} é par é: {resto2 == 0} e se é ímpar é: {resto2 != 0}")