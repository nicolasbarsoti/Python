#esse codigo foi traduzido do visualg

#aqui eu crio variaveis que irao pedir para o usuario digitar seu peso e tamando
p = float(input('Peso: '))
a = float(input('Altura: '))
#aqui e declarado a variavel IMC
IMC = float
#aqui e feito o calculo da conta que e IMC igual a variavel p dividida por a ao quadrado
IMC = p / (a**2)
print('IMC: ', IMC)
#aqui criamos condicionais que iráo determinar oque sera impresso em tela dependendo do que o usuario irá digitar e conforme o calculo feito
#aqui sera impresso em tela se IMC for menor ou igual a 17
if IMC <= 17:
    print('Muito abaixo do peso ')
else:
#aqui sera impresso em tela se IMC for maior ou igual a 18.5 e menor igual a 25
    if IMC >= 18.5 and IMC <= 25:
        print('Peso ideal')
    else: 
        #aqui sera impresso em tela se IMC for maior ou igual a 25 e menor igual a 30
        if IMC >= 25 and IMC <= 30:
            print('Acima do peso')
        else:
            #aqui sera impresso em tela se IMC for maior ou igual a 30 e menor igual a 35
            if IMC >= 30 and IMC <= 35:
                print ('Obesidade')
            else:
                #aqui sera impresso em tela se IMC for maior ou igual a 35 e menor igual a 40
                if IMC >= 35 and IMC <= 40:
                    print('Obesidade Severera')
                else:
                    #aqui sera impresso em tela se IMC for maior ou igual a 40 e menor igual a 45
                    if IMC >= 40 and IMC <= 45:
                        print('Obesidade Morbida')
                        
