    # a linha abaixo obtem o valor do produto sem desconto
vsd = float(input('Isira o valor do produto: '))
#  "vsd" e valor sem desconto

# a linha abaixo obtem o valor do desconto
vcd = float(input('Insira a percentagem de desconto: '))
# "vcd" e valor com desconto

# aqui calcula o valor do desconto
vd = vsd * vcd/100
#"vd" e valor do desconto

# Calculando o valor final com desconto
vfcd = vsd - vd
# "vfcd" e valor final com desconto

print("O valor descontado é de: ", (vd))
print("O valor a pagar é de: ", (vfcd))
