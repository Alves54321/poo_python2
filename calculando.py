def calcular_desconto(preco):
    porcentagem = preco * 0.10
    return porcentagem
desconto = calcular_desconto(200)
preco_final = 200 - desconto
print("Desconto aplicado:", desconto)
print("preco_final", preco_final)
print("_" *40)

#VOCÊ USA PARÂMETRO QUANDO UMA FUNÇÃO PRECISA RECEBER UMA INFORMAÇÃO DE FORA.
#PARÂMETRO = DADO QUE A FUNÇÃO PRECISA PARA FAZER SEU TRABALHO.

#TESTE 1
def somar(a, b):
    resultado = a + b
    return resultado

soma = somar(5, 3)
print(soma)
# Saída: 8
print("_" *40)

#TESTE 2
def somar(a, b):
    resultado = a + b
    print(resultado)
soma = somar(5, 3)
print(soma)
print("_" *40)

#TESTE 3
def somar(a, b):
    print(a + b)
x = somar(5, 3)
print("Valor em x:", x)
print("_" *40)

#TESTE 4
def somar(a, b):
    return a + b
x = somar(5, 3)
print("Valor em x:", x)
print("_" *40)