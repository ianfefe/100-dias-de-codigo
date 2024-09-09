def fatorial(n):
    if n <= 1:
        return 1

    else:
        return n * fatorial(n-1)
    
while True:

    numero = int(input("Digite o número que deseja saber o fatorial: "))
    print("O fatorial de ", numero, " é: ",fatorial(numero))

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if (continuar == 'n'):
        print("Calculadora fatorial encerrada.")
        break