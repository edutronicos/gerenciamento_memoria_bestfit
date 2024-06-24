from tabulate import tabulate


# Encontra o melhor bloco para inserir o processo que o usuario digitou.
def best_fit(blocos_memoria, processo_tamanho):
    melhor_indice = -1
    melhor_tamanho = None

    for i, tamanho in enumerate(blocos_memoria):
        if tamanho >= processo_tamanho:
            if melhor_tamanho is None or tamanho < melhor_tamanho:
                melhor_tamanho = tamanho
                melhor_indice = i

    # Se encontrou um bloco bom, aloca e retorna o índice
    if melhor_indice != -1:
        blocos_memoria[melhor_indice] -= processo_tamanho
        return melhor_indice
    else:
        return None
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


#Função que pega o tamanho original dos blocos de memória
def pega_memo_original(blocos_memoria):                                                 
    blocos_memoria_original = []  
    for i in range(len(blocos_memoria)):
        blocos_memoria_original.append(blocos_memoria[i])
    return blocos_memoria_original
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Função para realocar os processos.
def realocar_processos(blocos_memoria, processos_alocados, blocos_memoria_original):
    esp_livre = sum(blocos_memoria)                                                     # Calcula o espaço livre
    
    # Encontra os novos índices de alocação
    for i in range(len(blocos_memoria)):
        if len(blocos_memoria) == i + 1:
            blocos_memoria[i] = esp_livre
        elif processos_alocados[i] <= blocos_memoria_original[i]:
            blocos_memoria[i] = 0
        else:
            print("Não foi possível realocar os processos.")
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    
# Variáveis globais
blocos_memoria = [100, 150, 200, 300, 550, 780, 900]                                    # Tamanhos dos blocos de memória que irão ser alterados
blocos_memoria_original = pega_memo_original(blocos_memoria)                            # Tamanhos dos blocos de memória(original)
processos_alocados = [0] * len(blocos_memoria)                                          # Processos alocados em cada bloco de memória
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Aqui vai printar os blocos de memoria sempre no inicio
print("Alocação de Memória:")
print("-" * 22)

dados = []
headers = ["Bloco", "Tamanho", "Status"]
for i, tamanho in enumerate(blocos_memoria):
    # print(f"| Bloco {i}: {tamanho} (Livre) |")
    dados.append([f"Bloco {i}", tamanho, "Livre"])

tabela = tabulate(dados, headers=headers, tablefmt="grid")
print(tabela)
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Vai repetir 8 vezes para alocar 8 processos, pode escolher o numero de repetições alterando o numero dentro do range(*)
for i in range(8):
    processo_tamanho = int(input("Insira o tamanho do processo: "))
    indice_alocado = best_fit(blocos_memoria, processo_tamanho)

    if indice_alocado is not None:
        processos_alocados[indice_alocado] = processo_tamanho
        print(f"Processo alocado no bloco {indice_alocado}.")
    elif sum(blocos_memoria) == 0:
        print("Não há espaço livre para alocar o processo.")
        resposta = input("Deseja limpar todos os espaços de memoria ? (S/N) ")
        if resposta.upper() == "S":
            blocos_memoria = blocos_memoria_original.copy()
            processos_alocados = [0] * len(blocos_memoria)
            print("Memoria está totalmente limpa.")
    else:
        print("Não foi possível alocar o processo.")
        resposta = input("Deseja realocar os processos? (S/N) ")
        if resposta.upper() == "S":
            espaco_livre = sum(blocos_memoria)
            tamanho_original = sum(blocos_memoria_original)
            if espaco_livre >= processo_tamanho:
                realocar_processos(blocos_memoria, processos_alocados, blocos_memoria_original)
                print("Processos realocados com sucesso.")
        

    # Aqui vai printar os blocos de memoria sempre no final
    dados2 = []
    print("-" * 22)
    for i, tamanho in enumerate(blocos_memoria):
        status = "Ocupado" if processos_alocados[i] > 0 else "Livre"
        # print(f"| Bloco {i}: {tamanho} ({status}) |")
        dados2.append([f"Bloco {i}", tamanho, status])
    tabela = tabulate(dados2, headers=headers, tablefmt="grid")
    print(tabela)
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
