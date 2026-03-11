#1
print("\n")
print("Este programa ira coletar as informacoes do seu saldo\ne deposito, e depois dira o valor atualizado do saldo.")
print("\n")

saldo = (float(input("Digite seu saldo: ")))
dep = (float(input("Informe o valor que deseja depositar: ")))
print("\n")

saldo += dep

print("Seu saldo é de: ",saldo)
print("\n")

#2
print("\n")
print("Este programa ira calcular seu saldo de acordo com o orcamento que voce possui,\ne o valor que voce planeja gastar.")
print("\n")

orc = (float(input("Digite o orçamento que voce tem disponivel: ")))
gast = (float(input("Agora digite o gasto que pretende realizar: ")))
print("\n")

orc -= gast

print("Voce possui um saldo de:",orc)

#3
print("\n")
print("Este programa ira calcular a quantidade de itens atualizada do seu estoque.")

etqini = (int(input("Digite a quantidade de itens que seu estoque possui no inicio do dia: ")))
vend = (int(input("Agora digite a quantidade de itens que voce vendeu hoje: ")))
print("\n")

etqini -= vend

print("Seu estoque atual é: ", etqini)

#4
print("\n")
print("Este programa ira multiplicar por 3 qualuqer numero inteiro que voce fornecer.")
print("\n")

n = (int(input("Digite um numero qualquer: ")))
print("\n")

n *= 3

print("Este numero multiplicado por 3 é igual a ", n)

#5
print("\n")
print("Este programa ira mostrar em dias a quantidade de horas que voce informar.")
print("\n")

hora = (float(input("Digite uma quantidade de horas qualquer: ")))
print("\n")

hora /= 24

print("Esta quantidade de horas escrita em dias é igual a ", hora)

#6
print("\n")
print("Este programa ira mostrar em horas a quantidade de minutos que voce informar.")
print("\n")

min = (int(input("Digite uma quantidade inteira de minutos: ")))
print("\n")

min //= 60

print("Esta quantidade de minutos, escrita em horas, é igual a", min)

#7
print("\n")
print("Este programa ira mostrar em minutos qualquer quantidade de segundos que voce fornecer.")
print("\n")

seg = int(input("Digite uma quantidade inteira de segundos: "))
min = seg // 60

print("Esta quantidade de segundos, em minutos, e igual a", min)

#8
print("\n")
print("Este programa ira apresentar 0 para numeros pares, e 1 para numeros impares.")

n = (int(input("Digite um numero inteiro qualquer: ")))
print("\n")

res = n % 2

print(res)

#9
print("\n")
print("")
#Solicite um valor de estoque (int), subtraia as vendas utilizando -= 
#e depois a reposição do estoque utilizando +=, por fim, aplique %= 6.

est = (int(input("Informe seu estoque inicial: ")))
ven = (int(input("Informe o numero de vendas: ")))
rep = (int(input("Informe a quantidade de reposiçao efetuada: ")))
print("\n")

est -= ven
est += rep
est %= 6

print(est)