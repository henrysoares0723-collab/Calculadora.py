import math


# ---------- HISTÓRICO ----------

historico = []


def registrar_historico(operacao, num1, num2, resultado):
    registro = f"{num1} {operacao} {num2} = {resultado}"
    historico.append(registro)


def exibir_historico():
    print("\n" + "=" * 35)
    print("        HISTÓRICO DE CONTAS")
    print("=" * 35)
    if not historico:
        print("Nenhuma conta foi feita ainda.")
    else:
        for i, registro in enumerate(historico, start=1):
            print(f"{i}. {registro}")
    print("=" * 35 + "\n")


def limpar_historico():
    historico.clear()
    print("\nHistórico apagado com sucesso!\n")


# ---------- OPERAÇÕES ----------

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def potencia(a, b):
    return a ** b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo.")
    return math.sqrt(a)


def porcentagem(a, b):
    return (a * b) / 100


def resto(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular resto por zero.")
    return a % b
def fatorial(a):
    a = int(a)
    if a < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo.")
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i
    return resultado


def media(a, b):
    return (a + b) / 2
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9
# ---------- ENTRADA E MENU ----------

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")


def exibir_menu():
    print("=" * 35)
    print("        CALCULADORA PYTHON")
    print("=" * 35)
    print("1  - Somar")
    print("2  - Subtrair")
    print("3  - Multiplicar")
    print("4  - Dividir")
    print("5  - Potência")
    print("6  - Raiz quadrada")
    print("7  - Porcentagem")
    print("8  - Resto da divisão")
    print("9  - Ver histórico")
    print("10 - Limpar histórico")
    print("11 - Fatorial")
    print("12 - Média entre dois números")
    print("13 - Converter Celsius para Fahrenheit")
    print("14 - Converter Fahrenheit para Celsius")
    print("0  - Sair")
    print("=" * 35)

# ---------- PROGRAMA PRINCIPAL ----------

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nSaindo da calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"}:
            print("\nOpção inválida! Tente novamente.\n")
            continue

        if opcao == "9":
            exibir_historico()
            continue

        if opcao == "10":
            limpar_historico()
            continue

        try:
            if opcao == "6":
                num = ler_numero("Digite o número: ")
                resultado = raiz_quadrada(num)
                print(f"\nResultado: √{num} = {resultado}\n")
                registrar_historico("√", num, "", resultado)
            elif opcao == "11":
                num = ler_numero("Digite o número: ")
                resultado = fatorial(num)
                print(f"\nResultado: {int(num)}! = {resultado}\n")
                registrar_historico("!", num, "", resultado)
            elif opcao == "13":
                num = ler_numero("Digite a temperatura em Celsius: ")
                resultado = celsius_para_fahrenheit(num)
                print(f"\nResultado: {num}°C = {resultado}°F\n")
                registrar_historico("°C→°F", num, "", resultado)
            elif opcao == "14":
                num = ler_numero("Digite a temperatura em Fahrenheit: ")
                resultado = fahrenheit_para_celsius(num)
                print(f"\nResultado: {num}°F = {resultado}°C\n")
                registrar_historico("°F→°C", num, "", resultado)
            else:
                num1 = ler_numero("Digite o primeiro número: ")
                num2 = ler_numero("Digite o segundo número: ")

                if opcao == "1":
                    resultado = somar(num1, num2)
                    simbolo = "+"
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    simbolo = "-"
                elif opcao == "12":
                    resultado = media(num1, num2)
                    simbolo = "média"
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    simbolo = "*"
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    simbolo = "/"
                elif opcao == "5":
                    resultado = potencia(num1, num2)
                    simbolo = "^"
                elif opcao == "7":
                    resultado = porcentagem(num1, num2)
                    print(f"\nResultado: {num2}% de {num1} = {resultado}\n")
                    registrar_historico("%de", num1, num2, resultado)
                    input("Pressione ENTER para continuar...")
                    print()
                    continue
                elif opcao == "8":
                    resultado = resto(num1, num2)
                    simbolo = "%"

                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}\n")
                registrar_historico(simbolo, num1, num2, resultado)

        except (ZeroDivisionError, ValueError) as erro:
            print(f"\nErro: {erro}\n")

        input("Pressione ENTER para continuar...")
        print()


if __name__ == "__main__":
    main()
    # ---------- MEMÓRIA DA CALCULADORA ----------

memoria = 0.0

def memoria_adicionar(valor):
    global memoria
    memoria += valor
    print(f"\nValor {valor} adicionado à memória. (Memória atual: {memoria})\n")

def memoria_subtrair(valor):
    global memoria
    memoria -= valor
    print(f"\nValor {valor} subtraído da memória. (Memória atual: {memoria})\n")

def memoria_mostrar():
    print(f"\nValor atual armazenado na memória: {memoria}\n")

def memoria_limpar():
    global memoria
    memoria = 0.0
    print("\nMemória zerada com sucesso!\n")

def exibir_menu():
    print("=" * 35)
    print("        CALCULADORA PYTHON")
    print("=" * 35)
    print("1  - Somar")
    print("2  - Subtrair")
    print("3  - Multiplicar")
    print("4  - Dividir")
    print("5  - Potência")
    print("6  - Raiz quadrada")
    print("7  - Porcentagem")
    print("8  - Resto da divisão")
    print("9  - Ver histórico")
    print("10 - Limpar histórico")
    print("11 - Fatorial")
    print("12 - Média entre dois números")
    print("13 - Converter Celsius para Fahrenheit")
    print("14 - Converter Fahrenheit para Celsius")
    print("--- RECURSOS DE MEMÓRIA ---")
    print("15 - Mostrar valor da memória (MR)")
    print("16 - Limpar memória (MC)")
    print("17 - Adicionar último resultado à memória (M+)")
    print("18 - Subtrair último resultado da memória (M-)")
    print("0  - Sair")
    print("=" * 35)

    def main():
        ultimo_resultado = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nSaindo da calculadora. Até mais!")
            break

        opcoes_validas = {str(i) for i in range(1, 19)}
        if opcao not in opcoes_validas:
            print("\nOpção inválida! Tente novamente.\n")
            continue

        if opcao == "9":
            exibir_historico()
            input("Pressione ENTER para continuar...")
            continue

        if opcao == "10":
            limpar_historico()
            input("Pressione ENTER para continuar...")
            continue

        if opcao == "15":
            memoria_mostrar()
            input("Pressione ENTER para continuar...")
            continue

        if opcao == "16":
            memoria_limpar()
            input("Pressione ENTER para continuar...")
            continue

        if opcao in {"17", "18"}:
            if ultimo_resultado is None:
                print("\nNenhum cálculo recente para salvar na memória.\n")
            else:
                if opcao == "17":
                    memoria_adicionar(ultimo_resultado)
                else:
                    memoria_subtrair(ultimo_resultado)
            input("Pressione ENTER para continuar...")
            continue

        try:
            if opcao == "6":
                num = ler_numero("Digite o número: ")
                resultado = raiz_quadrada(num)
                print(f"\nResultado: √{num} = {resultado}\n")
                registrar_historico("√", num, "", resultado)
                ultimo_resultado = resultado
            elif opcao == "11":
                num = ler_numero("Digite o número: ")
                resultado = fatorial(num)
                print(f"\nResultado: {int(num)}! = {resultado}\n")
                registrar_historico("!", num, "", resultado)
                ultimo_resultado = resultado
            elif opcao == "13":
                num = ler_numero("Digite a temperatura em Celsius: ")
                resultado = celsius_para_fahrenheit(num)
                print(f"\nResultado: {num}°C = {resultado}°F\n")
                registrar_historico("°C→°F", num, "", resultado)
                ultimo_resultado = resultado
            elif opcao == "14":
                num = ler_numero("Digite a temperatura em Fahrenheit: ")
                resultado = fahrenheit_para_celsius(num)
                print(f"\nResultado: {num}°F = {resultado}°C\n")
                registrar_historico("°F→°C", num, "", resultado)
                ultimo_resultado = resultado
            else:
                num1 = ler_numero("Digite o primeiro número: ")
                num2 = ler_numero("Digite o segundo número: ")

                if opcao == "1":
                    resultado = somar(num1, num2)
                    simbolo = "+"
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    simbolo = "-"
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    simbolo = "*"
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    simbolo = "/"
                elif opcao == "5":
                    resultado = potencia(num1, num2)
                    simbolo = "^"
                elif opcao == "7":
                    resultado = porcentagem(num1, num2)
                    print(f"\nResultado: {num2}% de {num1} = {resultado}\n")
                    registrar_historico("%de", num1, num2, resultado)
                    ultimo_resultado = resultado
                    input("Pressione ENTER para continuar...")
                    print()
                    continue
                elif opcao == "8":
                    resultado = resto(num1, num2)
                    simbolo = "%"
                elif opcao == "12":
                    resultado = media(num1, num2)
                    simbolo = "média"

                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}\n")
                registrar_historico(simbolo, num1, num2, resultado)
                ultimo_resultado = resultado

        except (ZeroDivisionError, ValueError) as erro:
            print(f"\nErro: {erro}\n")

        input("Pressione ENTER para continuar...")
        print()

def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso / (altura ** 2)

def exibir_menu():
    print("19 - Calcular IMC")

def main():
    exibir_menu()
    altura = ler_numero("Digite a altura (m): ")
    resultado = calcular_imc(peso, altura)
    print(f"\nResultado: IMC = {resultado:.2f}\n")
    registrar_historico("IMC", peso, altura, resultado)
    ultimo_resultado = resultado
    