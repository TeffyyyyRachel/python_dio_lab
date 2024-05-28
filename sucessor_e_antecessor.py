def suc_ant(numero):
    sucessor = numero + 1
    antecessor = numero - 1
    return sucessor, antecessor
    
numero = int(input("Escolha um número: "))

resultado = list(suc_ant(numero))

print(f"O sucessor de {numero} é {resultado[0]}, e o antecessor, {resultado[1]}.")
