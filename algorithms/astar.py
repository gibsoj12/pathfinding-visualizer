class Node:

    def __init__(self, parent = None, position = None)
        self.parent = parent
        self.position = position

        self.g = 0 #dist between current node and start node
        self.h = 0 #estimated dist between current node and end node
        self.f = 0 # dist from start plus estimated dist from end (g + h)

    def __eq__(self, other):
        return (self.position == other.position)

    def set_g(self, val):
        self.g = val
    
    def set_h(self, val):
        self.h = val

    def set_f(self, val)
        self.f = val

def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.set_g(0)
    start_node.set_h(0)
    start_node.set_f(0)

    end_node = Node(None, end)
    end_node.set_g(0)
    end_node.set_h(0)
    end_node.set_f(0)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]