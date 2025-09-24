def Contador_palavra():
    
    frase = input("Digite uma frase: ").lower()
    palavra = input("Digite uma palavra para buscar: ").lower()

    palavras_frase = frase.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra:
            quantidade += 1
    
    return quantidade
