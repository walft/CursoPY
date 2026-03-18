'''
Interpolação básica de strings.
s - string
d e i - int
f - float
x e X -  hexadecimal (ABCDEF0123456789)
'''

nome = 'Luis'
preco = 1000.95897643
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco) # O objetivo é que essa variável receba Luis, o preço total foi de 1000.96, o % é o operador de formatação, o s é para string, o f é para float, e o .2 é para limitar a 2 casas decimais, o parenteses é para adicionar mais de um valor, se não tiver mais de um valor, ficava sem.
print(variavel)

# O hexadecimal é utilizado para representar números em base 16, onde os dígitos vão de 0 a 9 e as letras de A a F representam os valores de 10 a 15. Por exemplo, o número decimal 255 é representado como FF em hexadecimal.
print('O hexadecimal de %d é %x' % (15, 15)) # O %d é para inteiro, o %x é para hexadecimal, o resultado é O hexadecimal de 15 é f, pois o número 15 em hexadecimal é representado como F.
print('O hexadecimal de %d é %04x' % (15, 15)) # O %04x é para hexadecimal com 4 dígitos, o resultado é O hexadecimal de 15 é 000f, pois o número 15 em hexadecimal é representado como F, e o 0 é para preencher com zeros à esquerda até atingir 4 dígitos.
print('O hexadecimal de %d é %08X' % (1500, 1500)) # O %08X é para hexadecimal com 8 dígitos em maiúsculo, o resultado é O hexadecimal de 1500 é 05DC, pois o número 1500 em hexadecimal é representado como 5DC, e o 0 é para preencher com zeros à esquerda até atingir 8 dígitos.