# Precedência entre os operadores aritméticos
# 1. Parênteses (n + n)
# 2. Exponenciação n ** n
# 3. Multiplicação e divisão n * n, n / n, n // n, n % n
# 4. Adição e subtração n + n, n - n

conta_1 = 1 + 1 ** 5 + 5 # Fazendo a conta sem considerar a precedência, o resultado seria 1024, mas considerando a precedência, o resultado é 7
print(conta_1)
# Primeiro é feita a exponenciação, depois a adição, e por último a adição novamente. 1 ** 5 = 1, depois 1 + 1 = 2, e por último 2 + 5 = 7.

#outro exemplo:

conta_1 = (1 + (0.5 + 0.5)) ** (5 + 5) # Fazendo a conta sem considerar a precedência, o resultado seria 1024, mas considerando a precedência, o resultado é 1024
print(conta_1)
# Primeiro é feita a soma dentro dos parênteses, depois a soma dentro dos parênteses, e por último a exponenciação. (0.5 + 0.5) = 1, depois (1 + 1) = 2, e por último 2 ** 10 = 1024.
