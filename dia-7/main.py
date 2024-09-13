def tabuada(n):
        i = 1
        while i <= 10:
            print(n, " x ", i, " = ", i*n)
            i += 1

while True:

    numero = int(input("Digite o número que deseja saber a tabuada: "))
    tabuada(numero)

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if (continuar == 'n'):
        print("Tabuada encerrada.")
        break