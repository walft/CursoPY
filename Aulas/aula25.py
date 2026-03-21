"""
Fatiamento de strings

012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]

Obs: a função len retorna a qtd de caracteres da str.

"""

variavel = 'Olá mundo'
#print(variavel[4])
#print(variavel[-4])
#print(variavel[4:]) # somente o inicio, ao emitir o fim, ele vai retornar todo o restante depois da posição 4
#print(variavel[4:9]) # esse exemplo foi adicionado o fim do fateamento, sendo sempre 1 a mais pois a contagem começa em zero
#print(len(variavel))
print(variavel[0:9:1]) # passo, ele imprime os primeiros 9 elementos de variavel (do índice 0 até o 8), avançando de um em um.
print(variavel[0:9:2]) # Ele imprime os elementos de variavel do índice 0 até o 8, pulando de dois em dois (ou seja, os índices 0, 2, 4, 6 e 8).
print(variavel[::-1]) # Omitido inicio e fim e colocado negativo ele vai pegar de trás pra frente, invertendo o indice
