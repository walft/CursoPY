primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor})')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})')
else:
    print('Os valores não são válidos ou são igais.')

    