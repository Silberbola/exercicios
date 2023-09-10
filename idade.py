nome = input("Por favor digite o seu nome completo: ")
while True:
  try:
    anonasc = int(input("Digite o ano que você nasceu (válido de 1922 até 2021): "))
    if 1922 <= anonasc <= 2021:
      idade = (2022 - anonasc)
      print(nome, "em 2022 você completou", idade, "anos.")
      break
    else:
      print("Ano fora do intervalo permitido.")
  except ValueError:
      print("Por favor, digite um número válido para o ano de nascimento.")
