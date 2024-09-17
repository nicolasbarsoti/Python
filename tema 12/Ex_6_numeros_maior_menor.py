while True:
 cont = 1
 maior = -99999
 menor = 99999

 while cont <= 10:
    num = int(input("Digite um número ou digite o numero '0' para sair: "))
    if num == 0:
        print("Encerrando o programa.")
        
    else:
        print("Você digitou o número {num1}.")

    if cont == 1:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    cont += 1

 print ("O maior numero é ", maior, "e o número menor é", menor)
 break