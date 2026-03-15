'''
Aula 3 - Tipos de Dados STRING
DocStrings
Python é um tipo de liguagem de tipagem dinâmica, ou seja, não é necessário declarar o tipo de dado de uma variável, o Python irá inferir o tipo de dado a partir do valor atribuído a variável.

'''
print(1234)
#Aspas simples ou duplas podem ser utilizadas para criar strings, desde que sejam iguais no início e no final da string
print('Olá, mundo!')
print("Olá, mundo!")
print('"Olá, mundo!"') #utilizando aspas duplas para criar uma string que contém aspas simples
print('\'Olá, mundo!\'') #utilizando aspas simples para criar uma string, chamado de caracter de escape.
print(r"Olá, \"mundo!\"") #utilizando o caractere r para criar uma string raw, ou seja, uma string que não interpreta caracteres de escape, nesse caso, as aspas duplas serão interpretadas como parte da string e não como delimitadores de string.
# É realmente um problema quando se precisa utilizar aspas, mas o jeito mais simples é começar com outra aspas.