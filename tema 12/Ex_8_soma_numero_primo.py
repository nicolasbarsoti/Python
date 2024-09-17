#esse codigo está completamente imcompleto

for numero in range(0, 101):
    c = 0
    # Verifica quantos divisores o número possui
    for i in range(1, numero + 1):
        if numero % i == 0:
            c += 1
            print(i)
    # Verifica se o número é primo
    if c == 2:
        print(f"{numero} é um número primo.")