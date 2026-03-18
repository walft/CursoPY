'''
Formatação básica de strings 1
s - string
d - int
f - float
.< número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro

Sinal + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') # Adicionar 10 caracteres a direita, nesse caso de espaços
print(f'{variavel: <10}') # Adicionar 10 caracteres a esqueda, nesse caso de espaços, não é visível porque já estava alinhado a esquerda
print(f'{variavel: ^10}') # tenta alinhar ao centro
print(f'{variavel:$^10}') # tenta alinhar ao centro
print(f'{1000.12984693184710274184:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}') # Chamando método repr dentro da string
print(f'{variavel!s}') # Chamando método str dentro da string
print(f'{variavel!a}') # Chamando método ask dentro da string