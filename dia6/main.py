def fatorial(n):
    if n <= 1:
        return 1

    else:
        return n * fatorial(n-1)
    
numero = int(input("Digite o número que deseja saber o fatorial: "))

print("O fatorial de ", numero, " é: ",fatorial(numero))