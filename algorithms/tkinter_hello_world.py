import tkinter as tk

maze =      [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
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

for row_num in range(len(maze)):
    for column_num in range(len(maze[row_num])):
        if maze[row_num][column_num] == 0:
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = column_num, row = row_num)
            button = tk.Button(master=frame, bg="black").grid(column = column_num, row = row_num)
        else:
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth= 2).grid(column = column_num, row = row_num)
            button = tk.Button(master=frame, bg="white").grid(column = column_num, row = row_num)
window.mainloop()