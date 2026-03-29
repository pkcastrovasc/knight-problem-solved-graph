from graph import Graph
from cc import CC
from breadthfirstpaths import BreadthFirstPaths
from cycle import Cycle

def find_cycle_vertices(g):
    """Encontra um ciclo no grafo usando DFS"""
    n = g.V
    marked = [False] * n
    parent = [-1] * n
    cycle = []

    def dfs(v, p):
        marked[v] = True
        for w in g.adj[v]:
            if cycle:
                return True
            if not marked[w]:
                parent[w] = v
                if dfs(w, v):
                    return True
            elif w != p:
                # Ciclo encontrado, reconstruir caminho
                x = v
                cycle.append(w)
                while x != w:
                    cycle.append(x)
                    x = parent[x]
                cycle.append(w)
                cycle.reverse()
                return True
        return False

    for i in range(n):
        if not marked[i] and dfs(i, -1):
            break
    return cycle

with open("dados/entrada.txt") as f:
    V = int(f.readline())
    E = int(f.readline())
    Grafo = Graph(V)
    
    for _ in range(E):
        v, w = f.readline().split()
        Grafo.add_edge(v, w)

# Questao 1
print(Grafo)

print()
# Questao 2
vertice = 0
cc = CC(Grafo)
conectados = []

for i in range(Grafo.V):
    if cc.connected(vertice, i):
        conectados.append(i)

print("Vertices conectados a %d: %s" % (vertice, conectados))

print()
# Questao 3
bfs = BreadthFirstPaths(Grafo, vertice)

print(len(list(bfs.path_to(8)))-1)

print()
# Questao 4
cycle = Cycle(Grafo)
if cycle.has_cycle:
    print("Sim")
else:    
    print("Nao")

print()
# Questao 5
ciclo = find_cycle_vertices(Grafo)
if ciclo:
    # Rotacionar ciclo para começar no vértice 0
    if 0 in ciclo:
        idx = ciclo.index(0)
        ciclo_rotacionado = ciclo[idx:-1] + ciclo[:idx] + [0]
        ciclo_invertido = ciclo_rotacionado[::-1]
        print("Ciclo a partir de 0:", ciclo_invertido)
    else:
        print("Ciclo existe, mas não passa por 0:", ciclo)
else:
    print("Nao existe ciclo")
