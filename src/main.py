from graph import Graph
from cc import CC
from breadthfirstpaths import BreadthFirstPaths
from cycle import Cycle

def find_cycle_vertices(g):
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

def vertice_conectado(g, vertice):
    cc = CC(g)
    conectados = []
    for i in range(g.V):
        if cc.connected(vertice, i):
            conectados.append(i)
    return conectados


# Questao 1
with open("dados/entrada.txt") as f:
    V = int(f.readline())
    E = int(f.readline())
    Grafo = Graph(V)
    
    for _ in range(E):
        v, w = f.readline().split()
        Grafo.add_edge(v, w)

print(Grafo)

print()
# Questao 2
cc = CC(Grafo)

print("Numero de componentes conexas:", cc.count)
print()

print("Vertices conectados a componente 0:", vertice_conectado(Grafo, 0))
print("Vertices conectados a componente 1:", vertice_conectado(Grafo, 4))


print()
# Questao 3
bfs = BreadthFirstPaths(Grafo, 0)

print("Distancia minima de (0,0) até (2,2): %d" % (len(list(bfs.path_to(8)))))

print()
# Questao 4
cycle = Cycle(Grafo)
if cycle.has_cycle:
    print("O grafo possui ciclo: Sim")
else:    
    print("O grafo possui ciclo: Nao")

print()
# Questao 5
ciclo = find_cycle_vertices(Grafo)
if ciclo:
    if 0 in ciclo:
        idx = ciclo.index(0)
        ciclo_final = (ciclo[idx:-1] + ciclo[:idx] + [0])[::-1]
        print("Ciclo a partir de 0:", ciclo_final)
    else:
        print("Um ciclo encontrado:", ciclo)
else:
    print("Nao existe ciclo")
