def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    count = 0
    for letra in frase:
        if letra in vogais:
            count += 1
    return count


frase = input("Digite uma string: ")
total_vogais = contar_vogais(frase)
print(f"A string possui {total_vogais} vogais.")
