# ♟️ Projeto de Teoria dos Grafos: Caminho do Cavalo

Este repositório contém uma implementação em Python para manipulação de grafos, focada em identificar componentes conexas e calcular a distância mínima entre pontos em um tabuleiro de xadrez utilizando o movimento do cavalo.

## 🚀 Funcionalidades

O projeto está dividido em módulos principais:
- **Busca em Profundidade (DFS):** Utilizada na classe `CC` para encontrar e contar as **Componentes Conexas** do grafo.
- **Busca em Largura (BFS):** Utilizada na classe `BreadthFirstPaths` para encontrar o **menor caminho** (distância mínima) entre dois vértices.
- **Estruturas de Suporte:** Implementações de `Graph`, `Bag`, `Stack` e `Queue` para suporte aos algoritmos.

## 🧩 Problema do Cavalo
O algoritmo utiliza a **BFS** para determinar quantos movimentos um cavalo de xadrez precisa para ir da posição `(0,0)` até `(2,2)`. 
> **Resultado:** O cavalo leva no mínimo **4 movimentos** para atingir esse objetivo.

## 📂 Estrutura de Arquivos

```text
├── dados/
│   └── entrada.txt      # Arquivo com a estrutura do grafo (V e E)
├── src/
│   ├── graph.py         # Estrutura principal do Grafo
│   ├── cc.py            # Componentes Conexas (DFS)
│   ├── bfs.py           # Busca em Largura (Caminho mais curto)
│   └── main.py          # Script principal para execução
└── README.md
```

## 🛠️ Como Executar

1. Certifique-se de ter o Python 3.x instalado.
   
2. Clone o repositório
   ```
   git clone [https://github.com/SEU_USUARIO/t2-cavalo.git](https://github.com/SEU_USUARIO/t2-cavalo.git)
   ```
   
3. Execute o script principal:
   ```
   python src/main.py
   ```
   
## 📖 Conceitos Aplicados

- Grafos Não-Direcionados: Representação de conexões bidirecionais.
- Matriz vs Lista de Adjacência: Otimização de memória para busca de vizinhos.
- Complexidade de Algoritmos: Uso de BFS para garantir a otimização $O(V + E)$ na busca do caminho mínimo.

Desenvolvido por **Pedro Castro e Eduardo Suaki** como parte da disciplina de Teoria dos Grafos.
