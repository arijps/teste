n = int(input("Digite o número a ser pesquisado: "))
ultimo=1
penultimo=1


if (n==0) or (n==1) or (n==2):
    print("O número ", n, "pertence à squência de Fibonacci")
else:
    count=3
    while ultimo < n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)
    if (ultimo == n):
        print("O número ", n, "pertence à squência de Fibonacci")
    else:
        print("O número ", n, "não pertence à squência de Fibonacci")

