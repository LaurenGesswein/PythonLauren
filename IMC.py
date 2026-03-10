

print("Este programa ira calcular seu IMC.")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
print("\n")

imc = peso / (altura ** 2)

print("Seu IMC é ", imc)
print("\n")

bp = imc < 18.5
n = imc >= 18.5 and imc < 25
sb = imc >= 25 and imc < 30
ob = imc >= 30

print("Voce apresenta baixo peso.", bp)
print("Voce apresenta peso normal.", n)
print("Voce apresenta sobrepeso.", sb)
print("Voce apresenta obesidade.", ob)
print("\n")

print("Fim.")

