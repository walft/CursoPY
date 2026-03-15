# Usando a função input para coletar dados do usuário
#nome = input('Digite seu nome: ') # A função input é usada para coletar dados do usuário. O texto dentro dos parênteses é exibido como um prompt para o usuário. O valor digitado pelo usuário é armazenado na variável nome.
#print(f'O seu nome é {nome=}')

numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

print(f'O resultado da soma é: {numero1 + numero2}') # O resultado da soma é a concatenação das duas strings, não a soma dos números.
print(f'O resultado da soma é: {int(numero1) + int(numero2)}') # Para obter a soma dos números, é necessário converter as strings para inteiros usando a função int().

# Outra forma de converter as strings para inteiros é usando a função int() diretamente na função input(), assim não é necessário armazenar as strings em variáveis intermediárias, não é recomendado, pois caso o usuário digite um valor que não possa ser convertido é apresentado erro e o dado inserido não é armazenado, o que pode ser problemático para o programa.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(f'O resultado da soma é: {numero1 + numero2}')
