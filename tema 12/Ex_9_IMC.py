p = float(input('Peso: '))
a = float(input('Altura: '))
IMC = float
IMC = p / (a**2)
print('IMC: ', IMC)

if IMC <= 17:
    print('Muito abaixo do peso ')
else:
    if IMC >= 18.5 and IMC <= 25:
        print('Peso ideal')
    else: 
        if IMC >= 25 and IMC <= 30:
            print('Acima do peso')
        else:
            if IMC >= 30 and IMC <= 35:
                print ('Obesidade')
            else:
                if IMC >= 35 and IMC <= 40:
                    print('Obesidade Severera')
                else:
                    if IMC >= 40 and IMC <= 45:
                        print('Obesidade Morbida')
                        