# esse programa calcula quantas notas de 50,10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido
# a baixo eu declaro o valor das variaveis das notas
nc = float (50)
nd = float (10)
nu = float (1)
# "nc" e nota de 50, "nd" e nota de 10 e "nu" e nota de 1
 
# a linha abaixo obtem o valor da conta
vc = float (input("digite o valor da conta"))

# as linhas abaixo calcula o valor da nota de 50
v1 =  (vc // nc) 
vc = vc % nc
 

# as linhas abaixo calcula o valor da nota de 10
v2 = (vc // nd) 
vc = vc % nd


# as linhas abaixo calcula o valor da nota de 1
v3 = vc // nu
vc = vc % nu

print ("Para pagar a conta você precisará de : ")
print (v1, "notas de 50")
print (v2, "notas de 10")
print (v3, "notas de 1")