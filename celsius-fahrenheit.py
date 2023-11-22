def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade de temperatura (C para Celsius ou F para Fahrenheit): ")

if unidade.upper() == "C":
    fahrenheit = celsius_para_fahrenheit(temperatura)
    print("Temperatura em Fahrenheit:", fahrenheit)
elif unidade.upper() == "F":
    celsius = fahrenheit_para_celsius(temperatura)
    print("Temperatura em Celsius:", celsius)
else:
    print("Unidade de temperatura inválida. Digite C para Celsius ou F para Fahrenheit.")

print("\n")
print("Pressione Enter para continuar...")
input()  # Aguarda o usuário pressionar a tecla "Enter"

