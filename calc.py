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
    try:
        return a ** b
    except ZeroDivisionError:
        # Cobre o caso de 0 elevado a expoente negativo (0 ** -1, por exemplo)
        raise ZeroDivisionError("Não é possível elevar 0 a um expoente negativo.")
    except OverflowError:
        raise OverflowError("O resultado da potência é grande demais para ser calculado.")


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


# ---------- ENTRADA E MENU ----------

def ler_numero(mensagem):
    """
    Lê um número do usuário, validando a entrada.
    - Impede letras, símbolos ou texto vazio.
    - Aceita tanto ponto quanto vírgula como separador decimal.
    - Repete a pergunta até receber um valor numérico válido.
    """
    while True:
        entrada = input(mensagem).strip()

        if entrada == "":
            print("Entrada vazia. Digite um número válido.\n")
            continue

        # Permite que o usuário digite números com vírgula (ex: 3,5)
        entrada_normalizada = entrada.replace(",", ".")

        try:
            return float(entrada_normalizada)
        except ValueError:
            print(f"Entrada inválida: '{entrada}' não é um número. Digite apenas números.\n")


def ler_opcao(mensagem, opcoes_validas):
    """
    Lê a opção do menu, validando se é um número inteiro dentro das opções permitidas.
    """
    while True:
        entrada = input(mensagem).strip()

        if not entrada.isdigit():
            print(f"Opção inválida: '{entrada}'. Digite apenas o número da opção desejada.\n")
            continue

        if entrada not in opcoes_validas:
            print("Opção inválida! Escolha um número do menu.\n")
            continue

        return entrada


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
    print("0  - Sair")
    print("=" * 35)


# ---------- PROGRAMA PRINCIPAL ----------

OPCOES_VALIDAS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}


def main():
    while True:
        exibir_menu()
        opcao = ler_opcao("Escolha uma opção: ", OPCOES_VALIDAS)

        if opcao == "0":
            print("\nSaindo da calculadora. Até mais!")
            break

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
                    input("Pressione ENTER para continuar...")
                    print()
                    continue
                elif opcao == "8":
                    resultado = resto(num1, num2)
                    simbolo = "%"

                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}\n")
                registrar_historico(simbolo, num1, num2, resultado)

        except (ZeroDivisionError, ValueError, OverflowError) as erro:
            print(f"\nErro: {erro}\n")

        input("Pressione ENTER para continuar...")
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até mais!")