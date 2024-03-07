def inverter_string(string):
    # Converte caracteres em uma lista de strings
    character = list(string)
    
    #Pega o tamanho da string
    size = len(character)
    
    for i in range(size // 2):
        # Troca a posição dos caracteres
        character[i], character[size - i - 1] = character[size - i - 1], character[i]
    
    # Converte a lista novamente em uma string
    inverted_string = ''.join(character)
    
    return inverted_string

original_string = "Matheus"
inverted_string = inverter_string(original_string)
print("String original:", original_string)
print("String invertida:", inverted_string)