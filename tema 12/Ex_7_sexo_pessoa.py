#  aqui ´e definido as variáveis M e F como strings
M = "M"
F = "F"

# aqui e solicitado para o usuaria o valor das variaveis
sexo = input("Digite M para sexo masculino ou F para sexo feminino: ")

# aqui e verificado o valor solicidado pelo usuario e empresso em tela o resultado utilizando condicionais compostas 
if sexo == M:
    print("O sexo é Masculino")
elif sexo == F:
    print("O sexo é Feminino")
else:
    print("Entrada inválida. Por favor, digite M ou F.")
