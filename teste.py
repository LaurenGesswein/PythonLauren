# Atualizar elemento com uma operação

# Tarefa: Crie uma lista com três inteiros.
# Atualize o último elemento para a soma dos dois primeiros.
# Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

print("Vamos criar uma lista de números.")
print("\n")

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = int(input("Digite um último número inteiro: "))
print("\n")

lista = [num1, num2, num3]
print(lista)
print("\n")

print("Lista atualizada com o último elemento alterado para a soma dos dois primeiros:")
print("\n")

soma = num1 + num2
lista.remove(num3)
lista.append(soma)

print(lista)
print("\n")
