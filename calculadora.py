# Entrada
numero1 = input("Digite o primeiro número:")
numero2 = input("Digite o segundo numero:")

print("\tDigite + para adição\n"
      "\tDigite - para subtração\n"
      "\tDigite * para multiplicação\n"
      "\tDigite / para divição\n"
      )

operacao = input("Digite qual é a operação:")

# Processamento

equacao = f"{numero1} {operacao} {numero2}"

resultado = eval(equacao)

# Saida

print(resultado)
