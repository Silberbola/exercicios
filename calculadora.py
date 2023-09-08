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
    print(res)

""" Agora é só você chamar a função, onde os dois primeiros serão os valores a serem acldulados e terceiro será a
a operação a ser executada, use 1 para somar,2 para subtrair, 3 para multiplicar e 4 para dividir. No exemplo 
abaixo efetuamos a operação 17 x 5. """

calculadora(17,5,3)
