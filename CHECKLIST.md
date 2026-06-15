# 🛡️ Sistema de Álbum de Figurinhas - Checklist de Desenvolvimento

Este checklist detalha as etapas de desenvolvimento do sistema de gerenciamento e troca de figurinhas da Copa 2026, focando na implementação manual de estruturas de dados lineares e organização modular orientada a objetos.

## 1. Configuração, Infraestrutura e Documentação
- [x] Inicializar repositório Git e configurar `.gitignore`.
- [x] Criar e detalhar o arquivo `README.md`.
- [x] **Estrutura de Diretórios:** Criar as pastas `modelos/`, `estruturas/`, `dados/` e o arquivo `main.py`.

## 2. Modelagem de Dados (Entidades & Nodos)
- [x] **Classe `Figurinha`:** Implementar os atributos `id` (int), `nome` (str), `pais` (str) e `raridade` (str).
- [x] **Método Especial:** Adicionar o método `__str__` na classe `Figurinha` para exibição formatada.
- [x] **Classe `NodoLista`:** Criar o nó para a Lista Encadeada (armazenar objeto `Figurinha` e referência `proximo`).
- [x] **Classe `NodoFila`:** Criar o nó encadeado para a Fila FIFO (armazenar objeto `Figurinha` e referência `proximo`).

## 3. Implementação das Estruturas Manuais (Ponteiros Puros)
- [x] **Classe `Album` (Lista Encadeada Simples):**
    - [x] Implementar ponteiro `cabeca` e contador `tamanho`.
    - [x] Implementar algoritmo de **Inserção Dinâmica Ordenada** por ID.
    - [x] Implementar algoritmo de **Remoção por ID** com ajuste manual de ponteiros (antecessor/sucessor).
    - [x] Implementar mecanismo de **Busca Linear** multimutável (por ID, Nome ou País).
- [x] **Classe `Fila` (FIFO Sequencial por Nós):**
    - [x] Implementar ponteiros `inicio` e `fim`.
    - [x] Implementar método `enqueue` (inserção no fim).
    - [x] Implementar método `dequeue` (remoção do início).
    - [x] Implementar método `peek` (espiar o primeiro da fila) e `limpar`.

## 4. Lógica de Negócio (Álbum, Repetidas e Trocas)
- [x] **Redirecionamento Automático:** Lógica na inserção para verificar se a figurinha já existe no álbum e enviá-la para a lista de **Figurinhas Repetidas** (que também usa a estrutura `Album`).
- [x] **Controle de Progresso:** Implementar método para calcular em tempo real a porcentagem concluída do álbum (com base no total de figurinhas únicas inseridas).
- [x] **Fila de Propostas:** Lógica para registrar propostas de troca que entram na Fila FIFO.
- [x] **Sistema de Troca Automática:** Verificar se ambos os lados possuem os cromos repetidos necessários, executar a transação e mover o registro para o histórico.
- [x] **Instância de Histórico:** Garantir o registro imutável das trocas usando uma instância isolada da classe `Fila`.

## 5. Persistência de Dados
- [x] **Módulo de Persistência (`persistencia.py`):** Criar funções para manipular o arquivo JSON.
- [x] **Operação de Salvamento:** Serializar o estado atual do Álbum, das Figurinhas Repetidas e das Filas para o arquivo `dados/dados_album.json`.
- [x] **Operação de Carregamento:** Reconstruir todas as estruturas de nós na memória ao iniciar o programa a partir do arquivo JSON salvo.

## 6. Interface de Simulação e Robustez
- [x] **Menu Interativo (`main.py`):** Construir o fluxo de console para navegação nas funcionalidades (Inserir, Remover, Buscar, Ver Álbum, Ver Repetidas, Progresso, Propor Troca, Processar Trocas, Ver Histórico e Sair).
- [x] **Tratamento de Exceções:**
    - [x] Validar entradas numéricas (IDs).
    - [x] Tratar tentativas de remoção ou busca de figurinhas inexistentes.
    - [x] Validar propostas de troca com dados inválidos ou insuficientes.

## 7. Validação de Restrições Técnicas
- [x] **Restrição Absoluta:** Garantir que as coleções nativas do Python (`list`, `dict`, `set`, `deque`) **não** sejam usadas para substituir a lógica de ponteiros das estruturas principais.
- [x] **Entregas Incrementais:** Realizar commits organizados e frequentes no GitHub ao longo do desenvolvimento para comprovação de evolução do código.

---
*Status Atual: finalizado*