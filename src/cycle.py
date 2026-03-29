from graph import Graph


class Cycle:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.has_cycle = False
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w, v)
            elif w != u:
                self.has_cycle = True


if __name__ == "__main__":
    import sys
    f = open(sys.argv[1])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    cycle = Cycle(g)
    if cycle.has_cycle:
        print("Graph is cyclic")
    else:
        print("Graph is acyclic")