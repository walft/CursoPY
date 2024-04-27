# if / elif      / else
# se / se não se / se não
entrada = input('Você deseja [S]air ou [E]ntrar?')

if entrada == 'E':
    print('Você acaba de entrar')
elif entrada == 'S':
    print('Você saiu')
else:
    print('Você não inseriu uma opção válida!')