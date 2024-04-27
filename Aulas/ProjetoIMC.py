#Tentativa de criar uma calculadora de IMC

print('Seja bem-vindo(a), sou uma calculadora simples criada pelo Luis para realizar calculo de índice de massa corporal o IMC!')
nome = input('Para começar, me informe o seu nome: ')
print(f'Olá {nome}! chega de vamos começar... vou realizar umas perguntas e vou fornecer o seu IMC e a descrição do indice.')
peso = int(input('Por favor, informe seu peso: '))
altura = float(input('Agora sua altura em metros: '))
imc = peso / altura ** 2
print(f'Com base nas informações inseridas, seu IMC é {imc}. A classificação é:')
if imc < 16:
    print('Magreza Grau III')


