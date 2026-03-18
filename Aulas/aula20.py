# Operadores lógicos AND, OR e NOT
# and (e) or (ou) not (não)- Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0.'' False
# Também existe o tipo None que é
# usado para representar um não valor
'''
entrada = input(' [E]ntrar [S]air: ')
senha_digitada = input('Digite a senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # Para evitar abiguidade, é recomendado usar parênteses para deixar claro a ordem de avaliação, o que está dentro do parênteses é avaliado primeiro.
# Caso o usuário digite em caixa alta ou baixa o programa irá aceitar.
    print('Entrar')
else:
    print('Sair')
'''

# Avaliação de curto circuito
print( 0 or False or 0 or 'abc' or True) # True
avaliacao = 0 or False or 0 or 'abc' or True # True
print(avaliacao) # abc
senha =input('Senha: ') or 'Sem senha' # Se o usuário não digitar nada, a mensagem 'Sem senha' será exibida.
print(senha)
