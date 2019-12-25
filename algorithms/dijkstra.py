import sys
import heapq

class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize #initial distances are infinite
        self.visited = False #No nodes have been visited at the start
        self.previous = None

    def add_neighbour(self, neighbour, weight = 0):
        self.adjacent[neighbour] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def __lt__(self, other):
        return (self.id < other.id)

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + 'adjacent: ' + str([x.id for x in self.adjacent])

    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Node(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, origin, dest, value = 0):
        if origin not in self.vertices:
            self.add_vertex(origin)
        if dest not in self.vertices:
            self.add_vertex(dest)

        self.vertices[origin].add_neighbour(self.vertices[dest], value)
        self.vertices[dest].add_neighbour(self.vertices[origin], value)

    def get_vertices(self):
        return self.vertices.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    
def get_shortest(node, path):
    if node.previous:
        path.append(node.previous.get_id())
        get_shortest(node.previous, path)
    return

def dijkstra(graph, start, target):
    start.set_distance(0)

    unvisited = [(node.get_distance(), node) for node in graph]
    heapq.heapify(unvisited)

    while len(unvisited):
        #pop node with the smallest distance while there are still unvisited nodes
        unvis = heapq.heappop(unvisited)
        current = unvis[1]
        current.set_visited()

        for nexxt in current.adjacent:
            if nexxt.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(nexxt)

            if new_dist < nexxt.get_distance():
                nexxt.set_distance(new_dist)
                nexxt.set_previous(current)
                print ('updated path: current = ' + str(current.get_id()) + ' next = ' + str(nexxt.get_id()) + ' new_dist = ' + str(nexxt.get_distance()))
            else:
                print ('not updated')

        while len(unvisited):
            heapq.heappop(unvisited)
        
        unvisited = [(node.get_distance(), node) for node in graph if not node.visited]
        heapq.heapify(unvisited)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)


    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))
    
    target = g.get_vertex('e')
    path = [target.get_id()]
    get_shortest(target, path)
    print ('The shortest path is : ' + str((path[::-1])))
        