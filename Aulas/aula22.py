# Operadores in e not in
# Strings são iteráveis, navegável item por item
# 0 1 2 3
# L u i s
#-4-3-2-1

nome = 'Luis'
print(nome[2]) # Imprime a letra 'i'
print(nome[-2]) # Imprime a letra 'i'

# Para verificar se um valor existe dentro de um iterável, podemos usar o operador in:

print('u' in nome) # Imprime True, pois 'u' existe em 'Luis'
print('a' in nome) # Imprime False, pois 'a' não existe em 'Luis'

# O operador not in é o inverso, vai apresentar falso se o valor existir:
print('u' not in nome) # Imprime False, pois 'u' existe em 'Luis'
print('a' not in nome) # Imprime True, pois 'a' não existe em 'Luis'

# Mais de uma letra pode ser verificada:
print('Lu' in nome) # Imprime True, pois 'Lu' existe em 'Luis'
print('iz' in nome) # Imprime True, pois 'iz' existe em 'Luis'
print('uis' not in nome) # Imprime False, pois 'uis' existe em 'Luis'
print('Luiz' not in nome) # Imprime True, pois 'Luiz' não existe em 'Luis'

# Exemplo de pesquisa feita pelo usuário:
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} foi localizado em {nome}')
else:
    print(f'{encontrar} não foi localizado em {nome}')

cpf = '123.456.789-00'
cpf_sem_formato = (cpf[0:3] + cpf[4:7] + cpf[8:11] + cpf[12:14])
print(cpf_sem_formato) # Imprime '12345678900'