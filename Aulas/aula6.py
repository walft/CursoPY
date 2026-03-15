# Conversão de tipos, coerção.
# type convertion, typecasting, coercion.
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos: int, float, bool, str.

print(1 + 1)  # int quando somamos dois inteiros o resultado é a soma
print('A' + 'B')  # str quando se coloca textos ele é concatenado (juntado)
# obs: Quando um operador executa mais de uma função, em programação chamamos isso de polimorfismo.
# print(1 + '1')  # TypeError: não é possível somar um inteiro com uma string, são tipos diferentes.

# Python é uma linguagem de tipagem dinâmica e forte, o tipo é inferido na hora da execução e a conversão somente ocorrerá se for possível, caso contrário teremos um erro.

print('1', type('1'))  # str
print(int('1'), type(int('1')))  # int
print(int('1') + 1)  # Converte a string '1' para o inteiro 1, depois somamos com o inteiro 1, resultando em 2.
print(float('1') + 1)  # Converte a string '1' para o float 1.0, depois somamos com o inteiro 1, resultando em 2.0.

#Ptyhon executa os parenteces de dentro para fora.

# A conversão para boolean existem regras para isso.
print(bool(''))  # False, string vazia é considerada falsa
print(bool(' '))  # True, string com espaço é considerada verdadeira

# É possível converter numeros para string, mas o contrário nem sempre é possível, por exemplo, a string '1.5' não pode ser convertida para inteiro, mas pode ser convertida para float.
print(str(1))  # '1'
print(float(1))  # 1.0  