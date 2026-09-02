import math


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
    print("0  - Sair")
    print("=" * 35)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nSaindo da calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("\nOpção inválida! Tente novamente.\n")
            continue

        try:
            if opcao == "6":
                num = ler_numero("Digite o número: ")
                resultado = raiz_quadrada(num)
                print(f"\nResultado: √{num} = {resultado}\n")
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
                    continue
                elif opcao == "8":
                    resultado = resto(num1, num2)
                    simbolo = "%"

                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}\n")

        except (ZeroDivisionError, ValueError) as erro:
            print(f"\nErro: {erro}\n")

        input("Pressione ENTER para continuar...")
        print()


if __name__ == "__main__":
    main()