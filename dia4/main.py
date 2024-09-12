num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print("1 - soma")
print("2 - subtração")
print("3 - divisão")
print("4 - multiplicação")
operacao = int(input("Escolha a operação que deseja fazer: "))

if(operacao == 1):
    print(f"O resultado da soma é igual a: {num1 + num2}")

elif(operacao == 2):
    print(f"O resultado da subtracao é igual a: {num1 - num2}")

elif(operacao == 3):
    print(f"O resultado da divisao é igual a: {num1 / num2}")

elif(operacao == 4):
    print(f"O resultado da multiplicacao é igual a: {num1 * num2}")

else:
    print("Operação inexistente")