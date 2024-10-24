numero = int(input("Digite um número inteiro positivo: "))
soma_digitos = sum(int(digito) for digito in str(numero))
print(f"A soma dos dígitos do número {numero} é: {soma_digitos}")
