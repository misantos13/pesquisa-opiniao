# Projeto de Pesquisa de opinião
# Agenda 08 - Desenvolvimento de Sistemas I
# Autor: Camila Ferreira Santos
# Turma> TMD

# Declaração de variáveis
notaExcelente = 0
notaRuim = 0

# Estrutura de Repetição e coleta de dados
for x in range (50):
    print("\n-----------")
    print(f"Pesquisa {x + 1}")
    print("-----------")
    
    nomeCliente = input ("Seu nome: ")
    idadeCliente = int (input ("Sua idade: "))
    opiniaoCliente = input ("Seu grau de satisfação com o serviço (Excelente, Bom, Ruim): ")



    if opiniaoCliente == "Excelente" or opiniaoCliente == "excelente":
        notaExcelente += 1

    elif opiniaoCliente == "Ruim" or opiniaoCliente == "ruim":
        notaRuim += 1

# Apresentação dos Resultados
print("\n----------------------")
print("\nResultado da pesquisa")
print("\nClassificaram como Excelente: ", notaExcelente)
print("Classificaram como Ruim: ", notaRuim)