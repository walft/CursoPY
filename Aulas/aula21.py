'''
Operadores lógicos:
And (e) or (ou) not (não)
And todas as condições precisam ser verdadeiras, se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor são consideradas falsy.
0 0.0 '' False.
Também existe outro tipo None que é usada para representar um não valor.
'''

entrada = input('[E]entrar ou [S]air? ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrada')
else:
    print('Sair')

