# aqui e colocado para o usuario declarar o valor das variaveis
ni = int(input("Digite o numero inicial: "))
nf = int(input("Digite o numero final: "))
#aqui e utilizado uma condicional composta para prever uma açao para quando a condicional inicial for falsa
if ni > nf:
       print ("O numero final deve ser menor ou igual ao final. ")
else:
    #aqui e feito o calculo para declarar as variaveis na ordem correta 
    for i in range (ni,nf + 1):     
#aqui e empresso o resulatdo final na tela   
        print (" Os numeros iniciais e finais são: ", i)
    
    
