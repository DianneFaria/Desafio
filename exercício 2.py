def verifica_letra_a(texto):
    contador = 0
    texto_min = texto.lower()
    
    for caractere in texto_min:
        if caractere == 'a':
            contador += 1
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) no texto.")
    else:
        print("A letra 'a' não está presente no texto.")

texto = input("Digite uma string: ")
verifica_letra_a(texto)

#Com o método integrado count:

def verifica_letra_a(texto):
    texto_min = texto.lower()
    contador = texto_min.count('a')
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) no texto.")
    else:
        print("A letra 'a' não está presente no texto.")

texto = input("Digite uma string: ")
verifica_letra_a(texto)
