#esse programa exibe a entrada de 2 valores e imprima na tela e depois troque os valores impressos e exiba novamente na tela

x = float (input("Digite o valor X: "))
y = float (input("Digite o valor Y: "))

print (" ")
print (" O valor de X e Y: ", (x), (","), (y))

print(" ")
x, y = y, x

print (" O valor de X e Y: ", (x), (","), (y))