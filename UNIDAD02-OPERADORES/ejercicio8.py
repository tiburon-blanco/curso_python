# Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.
# La relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8

temperatura=float(input("Ingrese la temperatura en grados Fahrenheit: "))

celsius=float((temperatura-32)/1.8)

print("La conversion de grados Fahrenheit a Celsius es la siguiente: ", celsius)