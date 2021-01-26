from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)

        if self.directed is False:
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    def topoSortvisit(self, s, visited, sortlist):
        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortvisit(i, visited, sortlist)

        sortlist.insert(0, s)

    def topoSort(self):
        visited = {i: False for i in self.graph}

        sortlist = []

        for v in self.graph:
            if not visited[v]:
                self.topoSortvisit(v, visited, sortlist)

        print(sortlist)


if __name__ == '__main__':

    g = Graph(directed=True)

    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    print("Topological Sort:")
    g.topoSort()
