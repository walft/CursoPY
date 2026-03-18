# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Digite a senha: ')

if senha == '123456':
    print('Login realizado com sucesso!')
else:
    print('Senha incorreta.')

# Invertendo a expressão, mas o mesmo resultado é obtido

if senha != '123456':
    print('Senha incorreta.')

# String vazio é considerado False, ou seja, se o usuário não digitar nada, a senha será False, mesmo resultado.

if not senha:
    print('Você não digitou nada.')