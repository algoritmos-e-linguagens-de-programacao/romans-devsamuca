def int_para_romano(numero):
    if not (0 < numero < 4000):
        raise ValueError("Número deve estar entre 1 e 3999")

    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    resultado = []
    for valor, numeral in valores:
        while numero >= valor:
            resultado.append(numeral)
            numero -= valor

    return ''.join(resultado)

# Exemplo de uso
numero = int(input("Digite um número: "))
numero_romano = int_para_romano(numero)
print(f'O número {numero} em romano é: {numero_romano}')
