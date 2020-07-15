import numpy as np
import tkinter as tk

class Node:

    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0 #dist between current node and start node
        self.h = 0 #estimated dist between current node and end node
        self.f = 0 # dist from start plus estimated dist from end (g + h)

    def __eq__(self, other):
        return (self.position == other.position)

    def __str__(self):
        return str(self.position)

    def set_g(self, val):
        self.g = val
    
    def set_h(self, val):
        self.h = val

    def set_f(self, val):
        self.f = val

def update_window(col, row, window):
    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = col, row = row)
    button = tk.Button(master=frame, bg="red").grid(column = col, row = row)

def updater(col, row, window): #Gotta figure out how to update
    update_window(col, row, window)
    window.after(1000, updater(col, row, window))

def astar(maze, start, end, window):

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
            solution = [[0 for x in range(len(maze[numrows]))] for numrows in range(len(maze))]
            current = current_node
            while current is not None:
                update_window(current.position[1], current.position[0], window)
                #updater(current.position[1], current.position[0], window)
                solution[current.position[0]][current.position[1]] = 1
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []

        for new_position in [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]:

            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or node_pos[1] < 0:
                continue

            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            new_node = Node(current_node, node_pos)

            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.set_g(current_node.g + 1)
            child.set_h((child.position[0] - end_node.position[0]) ** 2 + ((child.position[1] - end_node.position[1]) ** 2))
            child.set_f(child.g + child.h)

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    window = tk.Tk()

    start = (0, 0)
    end = (7, 6)


    for row_num in range(len(maze)):
        for column_num in range(len(maze[row_num])):
            if (row_num == start[0] and column_num == start[1]) or (row_num == end[0] and column_num == end[1]):
                frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = column_num, row = row_num)
                button = tk.Button(master=frame, bg="red").grid(column = column_num, row = row_num)
            elif maze[row_num][column_num] == 0:
                frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = column_num, row = row_num)
                button = tk.Button(master=frame, bg="black").grid(column = column_num, row = row_num)
            else:
                frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = column_num, row = row_num)
                button = tk.Button(master=frame, bg="white").grid(column = column_num, row = row_num)


    path = astar(maze, end, start, window)

    window.mainloop()    

if __name__ == '__main__':
    main()           