'''
Introdução ao try / except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

'''

numero = input('Vou dobrar o valor digitado: ')

try:
    print('STR:', numero)
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro do valor digitado "{numero}" é {numero_float * 2:.2f}') # convertido para inteiro e multiplicado
except:
    print(f'Isso não é um numero')
#print(f'O dobro do valor digitado "{numero}" é {numero * 2}') # repetição
#print(f'O dobro do valor digitado "{numero}" é {int(numero) * 2}') # convertido para inteiro e multiplicado
#print(f'O dobro do valor digitado "{numero}" é {float(numero) * 2:.2f}') # convertido para inteiro e multiplicado
#if numero.isdigit():
#    print(f'O dobro do valor digitado "{numero}" é {int(numero) * 2}')
#else:
#    print('O numero digitado não é válido')