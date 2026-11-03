# Inicialização dos contadores
excelente = 0
bom = 0
ruim = 0

# Pesquisa com 50 entrevistados
for i in range(1, 51):

    print(f"\n--- Entrevistado {i} ---")

    # Coleta dos dados do entrevistado
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    # Contabilização das respostas
    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")

    elif opiniao == 2:
        bom += 1
        print("Opinião registrada: BOM")

    elif opiniao == 3:
        ruim += 1
        print("Opinião registrada: RUIM")

    else:
        print("Opinião inválida!")

# Exibição do resultado final
print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")