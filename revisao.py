#CONDICIONAIS 01
numero = int(input("Digite um número: "))
if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")    
else:
    print("zero")
print("_" *40)


#REPETIÇÃO FOR 02
for i in range(1 ,21):
    print("i")
print("_" *40)


#REPETIÇÃO WHILE 03
numero = int(input("Digite um número: "))
i = 0
while i <= numero:
    print(i)
    i += 1
print("_" *40)


#WHILE TRUE COM SAÍDA 04
while True:
    palavra = input("Digite uma palavra ou 'sair' para encerrar: ")
    if palavra.lower() == "sair":
         break
    print("Programa encerrado! ")
       
print("_" *40)


#TUPLA 05
cores = ("preto", "branco", "vermelho", "azul", "verde")
indice = int(input("Digite um indice de 0 a 4: "))
if 0 <= indice <= 4:
    print("A cor correspondente é: (cores[indice])")
else:
    print("indice inválido! ")
print("_" *40)


#LISTA 06
nomes = []

nome = input(f"Digite o nome: ")
nomes.append(nome)
print("Total de nomes cadrastados: ")
len(nomes)
print("_" *40)
len(nomes)