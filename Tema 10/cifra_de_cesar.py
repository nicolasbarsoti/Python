def cifra_de_cesar(mensagem, chave):
    # Inicializa a string que armazenará a mensagem criptografada
    mensagem_criptografada = ""
    
    # Itera sobre cada caractere na mensagem
    for caractere in mensagem:
        # Verifica se o caractere é uma letra
        if caractere.isalpha():
            # Define o valor de deslocamento com base se a letra é maiúscula ou minúscula
            deslocamento = 65 if caractere.isupper() else 97
            # Criptografa o caractere e adiciona à mensagem criptografada
            mensagem_criptografada += chr((ord(caractere) - deslocamento + chave) % 26 + deslocamento)
        else:
            # Se não for uma letra, adiciona o caractere original à mensagem criptografada
            mensagem_criptografada += caractere
    
    # Retorna a mensagem criptografada
    return mensagem_criptografada

# Solicita ao usuário que digite a mensagem a ser criptografada
mensagem = input("Digite a mensagem para criptografar: ")
# Solicita ao usuário que digite o valor da chave (deslocamento)
chave = int(input("Digite o valor da chave (deslocamento): "))
# Chama a função cifra_de_cesar para criptografar a mensagem
mensagem_criptografada = cifra_de_cesar(mensagem, chave)

# Exibe a mensagem criptografada
print("Mensagem criptografada:", mensagem_criptografada)
