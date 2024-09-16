# esse print imprime na tela o numero iniciale e final

ni = int(input("Digite o numero inicial: "))
nf = int(input("Digite o numero final: "))

if ni > nf:
       print ("O numero final deve ser menor ou igual ao final. ")
else:
    for i in range (ni,nf + 1):     
   
        print (i)
    
    
