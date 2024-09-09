def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1,n2):
    return n1 / n2

def calculadora():
    while True:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        print("1 - soma")
        print("2 - subtração")
        print("3 - divisão")
        print("4 - multiplicação")
        operacao = int(input("Escolha a operação que deseja fazer: "))

        if(operacao == 1):
            print("O resultado da soma é igual a: ", adicao(num1,num2))

        elif(operacao == 2):
            print("O resultado da subtração é igual a: ", subtracao(num1,num2))

        elif(operacao == 3):
            print("O resultado da multiplicação é igual a: ", multiplicacao(num1,num2))

        elif(operacao == 4):
            print("O resultado da divisão é igual a: ", divisao(num1,num2))

        else:
            print("Operação inexistente")

        continuar = input("Deseja fazer outra operação? (s/n): ")
        if (continuar == 'n'):
            print("Calculadora encerrada.")
            break

calculadora()