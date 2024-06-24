# Simulador de gerenciamento de memoria no metodo bestfit, com interação do usuário.
Este software implementa a estratégia de alocação de memória Best Fit, que visa otimizar o uso da memória ao alocar processos nos blocos de memória disponíveis de forma a minimizar o espaço desperdiçado. O software foi desenvolvido em Python e utiliza a biblioteca tabulate para exibir a alocação de memória em formato de tabela.
## Tecnologias Utilizadas
-	Python: Linguagem de programação utilizada para desenvolver o software.
-	Tabulate: Biblioteca Python utilizada para formatar a saída em formato de tabela.
## O software oferece as seguintes funcionalidades:
1.	Alocação de Processos: O usuário pode inserir o tamanho de processos, e o software busca o melhor bloco de memória para alocá-los usando a estratégia Best Fit.
2.	Visualização da Alocação: O software exibe o estado da memória em formato de tabela, mostrando quais blocos estão ocupados e quais estão livres.
3.	Liberação de Memória: Se não houver espaço suficiente para alocar um processo, o software oferece a opção de liberar a memória, removendo todos os processos alocados.
4.	Realocação de Processos: Se não houver espaço suficiente e o usuário não desejar liberar a memória, o software tenta realocar os processos para liberar espaço.
## INTERAÇÃO COM O USUÁRIO
- Bloco Fixo
1.	Execute o arquivo Python contendo o código.
2.	O software exibirá a tabela inicial com os blocos de memória livres.
3.	Insira o tamanho do processo quando solicitado.
4.	O software tentará alocar o processo e exibirá o resultado.
5.	Repita os passos 3 e 4 para alocar mais processos.
6.	Se não houver espaço suficiente, o software perguntará se você deseja liberar a memória ou realocar os processos.
- Bloco variável
1. Execute o arquivo Python contendo o código.
2. O software exibira a tabela na horizontal com os espaços livres.
3. Escolha uma das opções que aparecem no menu, digite o nome da opção conforme está escrito no menu.
4. **alocar:** Irá alocar um processo do tamanho N e irá perguntar qual o nome para o processo.
5. **excluir:** Irá perguntar o nome do processo que deseja excluir.
6. **realocar:** Ira realocar os processos deixando os epaços vazios todos juntos.
7. **sair:** Irá encerrar o programa.
## Instalação:
Para instalar a biblioteca tabulate, você pode usar o gerenciador de pacotes pip:
``` pip install tabulate ```

