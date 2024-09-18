#aqui e criado uma variavel para que o usuario possa digitar oque for solicitado
cpf = int(input('Digite seu CPF: '))
#aqui e utilizado uma condicional para determinar se o valor da variavel digitada pelo usuario for igual ao valor validado e sera impresso na tela resultado correspondente
if cpf == "12345678929":
    print('CPF validado corretamente!')
else:
    print('CPF incorreto, tente novamente.')
