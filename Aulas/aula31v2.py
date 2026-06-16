nome = input("Digite seu nome: ")
qtdLetras = len(nome)

if qtdLetras <= 4:
    print("Seu nome é curto")
elif qtdLetras == 5 or qtdLetras == 6:
    print("Seu nome tem o tamanho normal")
else:
    print("Seu nome é muito grande")