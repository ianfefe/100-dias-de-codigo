def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)
    
while True:

    numero = int(input("Digite o número que deseja saber o fatorial: "))
    print(f"O fatorial de {numero} é: ", "Inexistente" if numero < 0 else fatorial(numero))

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if (continuar == 'n'):
        print("Calculadora fatorial encerrada.")
        break