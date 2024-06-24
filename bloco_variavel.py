from tabulate import tabulate

def alocar_processo(memoria, tamanho, nome_processo):
    for inicio in range(len(memoria)):
        if memoria[inicio] == 0:
            tamanho_espaco = 0
            while inicio + tamanho_espaco < len(memoria) and memoria[inicio + tamanho_espaco] == 0:
                tamanho_espaco += 1
            if tamanho_espaco >= tamanho:
                for i in range(tamanho):
                    memoria[inicio + i] = nome_processo
                return True
    return False

def excluir_processo(memoria, nome_processo):
    for i in range(len(memoria)):
        if memoria[i] == nome_processo:
            memoria[i] = 0

def realocar_memoria(memoria):
    memoria_compactada = []
    for bloco in memoria:
        if bloco != 0:
            memoria_compactada.append(bloco)
    memoria_compactada.extend([0] * (len(memoria) - len(memoria_compactada)))
    return memoria_compactada

def visualizar_memoria(memoria):
    print(tabulate([memoria], tablefmt="fancy_grid", numalign="left", stralign="left"))

print("\n")
print("Simulador de alocação de memória")
print("Tamanho da memória: 40 blocos")
print("-----------------------------")

# Inicialização da memória
memoria = [0] * 40

while True:
    visualizar_memoria(memoria)

    acao = input("Escolha uma ação (alocar, excluir, realocar, sair): ")

    if acao == "alocar":
        tamanho = int(input("Tamanho do processo: "))
        nome_processo = input("Nome do processo: ")
        if not alocar_processo(memoria, tamanho, nome_processo):
            print("Não há espaço suficiente na memória.")
    elif acao == "excluir":
        nome_processo = input("Nome do processo a excluir: ")
        excluir_processo(memoria, nome_processo)
    elif acao == "realocar":
        memoria = realocar_memoria(memoria)
    elif acao == "sair":
        break
    else:
        print("Ação inválida.")
