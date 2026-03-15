# Formatação de Strings
# Fstrings, ou Formatação de Strings, é uma maneira de formatar strings em Python. Ela permite que você insira variáveis dentro de uma string de forma fácil e legível. Para usar fstrings, basta colocar um 'f' antes da string e usar chaves {} para incluir as variáveis que você deseja inserir.

nome = 'Luis Henrique'
altura = 1.75
peso = 75.80
imc = peso / altura ** 2
salario = 12600.5

linha = f'Seu nome é {nome}, sua altura é {altura} em métros, seu peso atual é de {peso} kg, e seu IMC é de {imc:.2f}, e seu salário é de R$ {salario:.2f}.' # O :.2f é usado para formatar o número com 2 casas decimais, ou no caso do salário, para formatar o número com 2 casas decimais e o símbolo de moeda.
print(linha)
#formatação de string, usando o f antes da string, e as chaves para colocar as variáveis dentro da string.
