""" Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0. """


def calculadora (valor1, valor2, operacao):
    if operacao == 1:
        res = valor1 + valor2
    elif operacao == 2:
        res = valor1 - valor2
    elif operacao == 3:
        res = valor1 * valor2
    elif operacao == 4:
        res = valor1 / valor2
    else:
        res = 0
    print("O resulatado da opração é:", res)
    print("\n")

""" Agora é só você chamar a função, onde os dois primeiros serão os valores a serem acldulados e terceiro será a
a operação a ser executada, use 1 para somar,2 para subtrair, 3 para multiplicar e 4 para dividir. No exemplo 
abaixo efetuamos a operação 17 x 5. """
while True:
    print("Olá! \U0001F609 Digite o número referente à operação você deseja:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair")
    operacao = int(input())
    if operacao == 0:
        print("Até mais \U0001F44B e obrigado por usar a nossa calculaora.")
        break
    elif operacao ==1 or operacao ==2 or operacao ==3 or operacao ==4:
        print("Digite o primeiro valor:")
        valor1 = int(input())
        print("Digite o segundo valor:")
        valor2 = int(input())
        calculadora(valor1, valor2, operacao)
    else:
        print("Esta não é uma opção válida.\U0001F648")
        print('\n')