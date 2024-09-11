def celsiusToFahrenheit(tempC):
    tempF = (tempC * (9/5) + 32)
    return tempF

temperatura = int(input("Qual a temperatura em graus celsius? "))

print("A temperatura ", temperatura, "C em Fahrenheit é: ", celsiusToFahrenheit(temperatura), "F")