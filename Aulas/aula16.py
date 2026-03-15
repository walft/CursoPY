# Introdução aos blocos de código + if / elif / else (condicionais)
# if / elif / else são estruturas de controle de fluxo que permitem executar diferentes blocos de código com base em condições específicas. O bloco de código dentro do if é executado se a condição for verdadeira, o bloco de código dentro do elif é executado se a condição do if for falsa e a condição do elif for verdadeira, e o bloco de código dentro do else é executado se todas as condições anteriores forem falsas.

# SE / SE NÃO SE / SE NÃO

entrada = input("Você quer 'entrar' ou 'sair'? ")

# O if somente executa a primeira condição verdadeira.

if entrada == 'entrar': # O bloco de código dentro do if será executado se a condição for verdadeira (entrada == 'entrar').
    print('Você entrou no sistema.') # Este código será executado se a condição do if for verdadeira.
elif entrada == 'sair': # O bloco de código dentro do elif será executado se a condição do if for falsa e a condição do elif for verdadeira (entrada == 'sair').
    print('Você saiu do sistema.') # Este código será executado se a condição do if for falsa e a condição do elif for verdadeira.
else: # O bloco de código dentro do else será executado se todas as condições anteriores forem falsas.
    print('Entrada inválida. Por favor, digite "entrar" ou "sair".') # Este código será executado se todas as condições anteriores forem falsas (entrada diferente de 'entrar' e 'sair').