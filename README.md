

# estrutura-de-decis-o-e-repeti-o

1) Faça um algoritmo que exiba os números pares de 0 a 30 com exceção dos números 10, 20 e 30. Dica: utilize o comando for, break ou continue.


for i in range(0, 31, 2):  # percorre de 0 a 30, de 2 em 2 (números pares)
    if i in [10, 20, 30]:  # verifica se o número deve ser ignorado
        continue  # pula a exibição dos números 10, 20 e 30
    print(i)


2) Faça um algoritmo que calcule a média aritmética de um aluno que será exibida na tela a partir de suas duas notas.O algoritmo terá que informar se o aluno foi aprovado ou reprovado, sabendo que a média para ser aprovado é 6.
# Faça com que o usuário não consiga digitar notas menores que 0 e maiores que 10. Dica: utilize o comando while.

nota1 = float(input("Digite a primeira nota (entre 0 e 10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota (entre 0 e 10): "))

nota2 = float(input("Digite a segunda nota (entre 0 e 10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota (entre 0 e 10): "))

media = (nota1 + nota2) / 2

print(f"\nMédia: {media:.2f}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
