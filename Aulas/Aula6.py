# conversão de tipos, correção type convertion, typecasting, coercion é o ato de coverter um tipo em outro tipos imutáveeis e primitivos: str, int, float, bool.
print(1 + 1) # Dois tipos inteiros, será realizada a soma.
print('Luis ' + 'Henrique') # Duas string será concatenado

texto = '123'
print(type(texto))
print('Conversão do para inteiro ', texto, type(int(texto)))

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')