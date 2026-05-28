print('Seja bem-vindo(a) a calculador de Indice de Massa Corporal (IMC) esse aplicativo foi desenvolvido por: Luis Henrique Gonlçalves em 15/03/2026!')
concentimento = input('Vamos começar! Vou precisar de algumas informações para calcular seu IMC, tudo bem? digite "S" para sim ou "N" para não: ')
if concentimento.upper() == 'S':
    nome = input('Digite seu nome: ')
    peso = input('Digite seu peso em kg: ')
    altura = input('Digite sua altura em metros: ')
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        print(f'humm, tenho algo importante para te falar {nome}, seu IMC é {imc:.2f} e de acordo com a Organização Mundial da Saúde, você está abaixo do peso ideal (Magreza). É importante cuidar da sua saúde e procurar um profissional para orientações sobre alimentação e exercícios físicos.')
    elif 18.5 <= imc < 25:
        print(f'Parabéns {nome}, seu IMC é {imc:.2f} e de acordo com a Organização Mundial da Saúde, você está dentro do peso ideal (Normal). Continue cuidando da sua saúde com uma alimentação equilibrada e prática regular de exercícios físicos!')
    elif 25 <= imc < 30:
        print(f'Olá {nome}, seu IMC é {imc:.2f} e de acordo com a Organização Mundial da Saúde, você está acima do peso ideal (Sobrepeso). É importante cuidar da sua saúde e procurar um profissional para orientações sobre alimentação e exercícios físicos.')
    elif 30 <= imc < 39.9:
        print(f'Olá {nome}, seu IMC é {imc:.2f} e de acordo com a Organização Mundial da Saúde, você está com obesidade grau I (Obesidade). É importante cuidar da sua saúde e procurar um profissional para orientações sobre alimentação e exercícios físicos.')
    elif imc >= 40:
        print(f'Olá {nome}, seu IMC é {imc:.2f} e de acordo com a Organização Mundial da Saúde, você está com obesidade grau II (Obesidade Grave). É importante cuidar da sua saúde e procurar um profissional para orientações sobre alimentação e exercícios físicos.')
elif concentimento.upper() == 'N':
    print('Tudo bem, se mudar de ideia é só executar o programa novamente. Tenha um ótimo dia!')
else:
    print('Opção inválida. Por favor, execute o programa novamente e digite "S" para sim ou "N" para não.')

avaliacao = input('Qual nota você daria para esse aplicativo de 0 a 10? onde 0 é péssimo :(, 5 é regular :| e 10 é excelente :): ')
avaliacao = int(avaliacao)

if avaliacao < 5:
    print ('Que pena que você não gostou do aplicativo, mas agradeço pelo seu feedback! Ele é muito importante para mim e me ajuda a melhorar cada vez mais.')
else:
    print('Fico muito feliz que você gostou do aplicativo, agradeço pelo seu feedback! Ele é muito importante para mim e me ajuda a melhorar cada vez mais.')
