# Formatação de strings com o método format
a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c) # O método format é usado para formatar strings, onde os valores entre chaves {} são substituídos pelos argumentos passados para o método. Neste caso, a é substituído por 'A', b por 'B' e c por 1.1, formatado com duas casas decimais. O resultado é a string 'a=A b=B c=1.10'.
print(formato)

formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c) # Agora, por indice, onde os números dentro das chaves indicam a posição dos argumentos passados para o método format. O resultado é o mesmo que o exemplo anterior.
print(formato)
formato = 'a={1} b={0} c={2:.2f}'.format(a, b, c) # Aqui, a e b estão invertidos, pois os índices foram trocados. O resultado é a string 'a=B b=A c=1.10'.
print(formato)

# Agora, usando nomes para os argumentos, onde os nomes dentro das chaves correspondem aos nomes dos argumentos passados para o método format. O resultado é o mesmo que o exemplo anterior, porém agora os argumentos estão nomeados, onde um for nomeado todos os demais também precisam ser nomeados, e para ser utilizados devem ser chamados pelo nome, e não mais por índice.
formato = 'a={nome1} b={nome2} c={nome3:.2f}'.format(
    nome1=a,
    nome2=b,
    nome3=c
    )

print(formato)
