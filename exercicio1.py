for i in range(0, 31, 2):  # percorre de 0 a 30, de 2 em 2 (números pares)
    if i in [10, 20, 30]:  # verifica se o número deve ser ignorado
        continue  # pula a exibição dos números 10, 20 e 30
    print(i)