# Sistema de Álbum de Figurinhas - Copa 2026

Este projeto consiste em um sistema completo para gerenciamento, organização e troca de figurinhas da Copa do Mundo de 2026, desenvolvido como parte da disciplina de Estrutura de Dados da Fatec Rio Claro. 

O sistema simula a experiência real de colecionar um álbum, gerenciar figurinhas repetidas e registrar o histórico de trocas, utilizando estruturas de dados clássicas e lineares implementadas de forma nativa e manual: **Listas Encadeadas** e **Filas FIFO (First-In, First-Out)**.

## Estruturas de Dados Utilizadas

Para garantir o pleno domínio sobre a alocação de memória e a lógica dos ponteiros, o projeto não utiliza as listas (`list`) ou dicionários (`dict`) nativos do Python para o armazenamento principal. Em vez disso, foram construídas as seguintes estruturas:

### 1. Lista Encadeada Simples (Álbum)
Utilizada para representar o álbum de figurinhas do usuário de forma ordenada e dinâmica.
* **`Figurinha` (Entidade):** Contém os atributos fundamentais de cada cromo: `id` (int), `nome` (str), `pais` (str), `posicao` (str) e `raridade` (str).
* **`NodoLista`:** Objeto nó que armazena a instância da `Figurinha` e uma referência (`proximo`) para o próximo nó da lista.
* **`Album`:** Classe controladora da lista encadeada. Contém o ponteiro `cabeca` e o controle de `tamanho`. Implementa os algoritmos de inserção ordenada, remoção por ID, busca linear e cálculo de completude.

### 2. Fila FIFO (Trocas e Histórico)
Utilizada para gerenciar a ordem de processamento das trocas de figurinhas e o registro cronológico de eventos.
* **`NodoFila`:** Objeto nó que encapsula a `Figurinha` e aponta para o próximo elemento da fila.
* **`Fila`:** Implementação própria de uma fila sequencial baseada em ponteiros (`inicio` e `fim`). Suporta as operações fundamentais `enqueue()`, `dequeue()`, `peek()` e `limpar()`.
* **`Histórico`:** Uma instância separada da classe `Fila` dedicada exclusivamente ao registro imutável de todas as transações e trocas bem-sucedidas realizadas no sistema.

## Funcionalidades Principais

### Gerenciamento do Álbum e Repetidas
* **Inserção Dinâmica:** Adiciona novas figurinhas ao álbum mantendo uma ordenação lógica. Caso o usuário já possua a figurinha, o sistema a direciona automaticamente para a estrutura de **Figurinhas Repetidas**.
* **Controle de Repetidas:** Armazena, contabiliza e lista todas as figurinhas repetidas disponíveis para troca.
* **Remoção de Itens:** Permite retirar figurinhas do álbum.
* **Consultas Customizadas:** Mecanismo de busca linear que permite localizar cromos por:
  * Número (ID) da figurinha
  * Nome do jogador
  * Seleção / País
* **Progresso do Colecionador:** Calcula em tempo real a porcentagem concluída do álbum.

### Sistema de Trocas Inteligente & Persistência
* **Propostas de Troca:** Permite registrar propostas que entram em uma Fila FIFO.
* **Troca Automática:** O sistema verifica se os dois lados da transação possuem as figurinhas repetidas necessárias e efetua a troca automaticamente, movendo o registro para o Histórico.
* **Persistência de Dados:** O sistema salva e carrega o estado do álbum e das filas através de arquivos JSON, garantindo que os dados não sejam perdidos ao fechar o programa.

### Execução:

**Execute o projeto:**
    python main.py

## Organização do Projeto

O código-fonte está estruturado de forma modular e clara, separando as responsabilidades de cada componente para facilitar a manutenção e legibilidade:

```text
├── dados/
│   └── dados_album.json    # Arquivo de texto local para armazenamento dos dados
├── estruturas/
│   ├── album.py           # Implementação da Lista Encadeada (Álbum)
│   └── fila.py            # Implementação da Fila FIFO e Histórico
│   └── persistencia.py    # Funções de leitura e escrita de arquivos JSON
├── modelos/
│   ├── figurinha.py       # Definição da entidade Figurinha
│   ├── nodos.py           # Estrutura do nó para a Fila FIFO e Lista Encadeada
├── CHECKLIST.md           # Detalha as etapas de desenvolvimento do projeto
├── main.py                # Ponto de entrada do sistema e interface de simulação
└── README.md              # Documentação do projeto
```

---

### Status do Projeto:
*Em andamento*