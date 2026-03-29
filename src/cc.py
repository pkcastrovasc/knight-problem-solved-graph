from bag import Bag
from graph import Graph


class CC:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self.count = 0

        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

if __name__ == "__main__":
    import sys
    f = open(sys.argv[1])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    cc = CC(g)
    print(cc.count, " components")
    components = []
    for i in range(cc.count):
        components.append(Bag())

    for v in range(g.V):
        components[cc.id[v]].add(v)

    for i in range(cc.count):
        for v in components[i]:
            print(v, " ", end='')
        print()