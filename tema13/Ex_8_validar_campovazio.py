#aqui e criado uma variavel para que o usuario possa digitar oque for solicitado
c = input('Digite algo: ')
#aqui e utilizado uma condicional para determinar se o valor da variavel digitada pelo usuario for igual ao valor validado e sera impresso na tela resultado correspondente
if c == '':
    print('Campo vazio validado corretamente!')
else:
    print('Campo vazio incorreto, tente novamente.')
