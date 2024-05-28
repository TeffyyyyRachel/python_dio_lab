def soma(a, b):
    return a + b
    
def sub(a, b):
    return a - b

def mult(a, b):
    return a * b
    
def div(a, b):
    return a / b

def matematica(funcao, a, b):
    resultado = funcao(a,b)
    print(f"""      O resultado da operação é igual a {resultado:.2f}.""")

while True:
    escolha = int(input(""" 
            == MATEMATICA ==
        1- Somar dois números
        2- Subtrair dois números
        3- Multiplicar dois números
        4- Dividir dois números
        
        Escolha: """))
        
    
    if escolha == 1:
        escolha = soma
    elif escolha == 2:
        escolha = sub
    elif escolha == 3:
        escolha = mult
    elif escolha == 4:
        escolha = div
    else:
        print("Tente uma opção válida.")
    
    num1 = int(input("""      Primeiro número: """))
    num2 = int(input("""      Segundo número: """))
    
    matematica(escolha, num1, num2)
    








