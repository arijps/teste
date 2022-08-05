str = input("Digite uma string:")
caracteres = []
invertido = ''

for letra in str:
    caracteres.append(letra)

tamanho = len(caracteres) - 1

while tamanho >= 0:
    invertido += (caracteres[tamanho])
    tamanho -= 1

print("String invertida: ")
print(invertido)