phyton
# Calculadora Inteligente 1.0

def calculadora():
    while True:
        print("\n=== Calculadora Inteligente ===")
                                                                                                                                                                                                        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            continue                                 

        print("\nEscolha a operação:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")

        escolha = input("Qual a operação que você deseja realizar? (1/2/3/4): ")

        if escolha == '1':
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitido.")
        else:
            print("\nOperação inválida. Por favor, escolha 1, 2, 3 ou 4.")

        continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if continuar != 's':
            print("\nObrigado por usar a Calculadora Inteligente. Até a próxima!")
            break

# Executa a calculadora
calculadora()
