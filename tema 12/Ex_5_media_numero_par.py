#aqui e criado um laço de repetiçao para efetuar um loop ate que acondiçao seja verdadeira
while True:
    # as linhas abaixo solicitam os numeros do usuario
    num1 = int(input("Digite o numero 1 (ou 0 para sair): ")) 
    #aqui e feito a condiçao de saida
    if num1 == 0:
        print("Encerrando o programa.")
        break
    num2 = int(input("Digite o numero 2: ")) 
    num3 = int(input("Digite o numero 3: ")) 
    num4 = int(input("Digite o numero 4: ")) 
    num5 = int(input("Digite o numero 5: ")) 

    # aqui e criado uma lista com os numeros solicitados pelo usuario
    numeros = [num1, num2, num3, num4, num5]

    # aqui e feito o calculo da soma dos numeros
    soma = sum(numeros)

    # e aqui e feito a media da somas do numeros
    media = soma / len(numeros)

    # aqui e empresso na tela os resultados
    if media % 2 == 0:
        print("A média dos números é par:", media)
    else:
        print("A média dos números é ímpar:", media)
