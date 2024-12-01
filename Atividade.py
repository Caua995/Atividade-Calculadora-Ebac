#from os import system

# Variaveis do Programa
valor_resposta = 0
print("=="*10)
valor_total = float(input("Digite o Valor para fazer a operação: "))

# estrutura principal
while True:
    # Menu
    #system("cls")
    print("=="*10)
    print("        Menu")
    print("=="*10)
    print(f" Valor: {valor_total}")
    print("==" * 10)
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Fecha Programa")
    print("==" * 10)
    resposta = float(input("Digite um numero: "))

    # Ver Fecha Programa
    if resposta == 5:
        break

    # Ver soma
    elif resposta == 1:
        valor_resposta = float(input("Digite o valor da soma: "))
        print("==" * 10)
        print(f"{valor_total} + {valor_resposta} é igual a {valor_total+valor_resposta}")
        print("==" * 10)
        valor_total += valor_resposta
        print("presone enter para continua: ", end="")
        input("")

    # Ver Subtração
    elif resposta == 2:
        valor_resposta = float(input("Digite o valor da subtração: "))
        print("==" * 10)
        print(f"{valor_total} - {valor_resposta} é igual a {valor_total - valor_resposta}")
        print("==" * 10)
        valor_total -= valor_resposta
        print("presone enter para continua: ", end="")
        input("")

    # Ver Multiplicação
    elif resposta == 3:
        valor_resposta = float(input("Digite o valor da Multiplicação: "))
        print("==" * 10)
        print(f"{valor_total} X {valor_resposta} é igual a {valor_total * valor_resposta}")
        print("==" * 10)
        valor_total *= valor_resposta
        print("presone enter para continua: ", end="")
        input("")

    # Ver Divisão
    elif resposta == 4:
        valor_resposta = float(input("Digite o valor da Divisão: "))
        print("==" * 10)
        print(f"{valor_total} / {valor_resposta} é igual a {valor_total / valor_resposta}")
        print("==" * 10)
        valor_total /= valor_resposta
        print("presone enter para continua: ", end="")
        input("")
