from queue import Queue
from tkinter import Canvas, Tk
from fieldReader import get_field

SIZE = 600
FIELD = get_field("field2.csv")
SPEED = 10
DOT_SIZE = 15
LINE_COLOR = "#ff01c8"
DOT_COLOR = "white"
POINT_COLOR = "black"
OPEN_DOT_COLOR = "#cdffcd"
CLOSE_DOT_COLOR = "#ffcdcd"

class dot(object):
    def __init__(self, i, j, id_, available, parent = None, G = 0, H = 0):
        self.i = i
        self.j = j
        self.id_ = id_
        self.G = G
        self.H = H
        self.F = G + H
        self.parent = parent
        self.available = available



def draw_field(root, field, dot_size = 30):
    global DOT_COLOR, POINT_COLOR
    offset = dot_size / (2 * 2) #понятно почему так
    width = len(field[0])
    height = len(field)

    canvas = Canvas(
        root,
        width=width*dot_size,
        height=height*dot_size,
        bg="white",
        highlightthickness=0
    )
    canvas.pack()
    canvas.a_dots = []
    for i in range(height):
        canvas.a_dots.append([])
        for j in range(width):
            
            dot_ = dot(
                i,
                j,
                canvas.create_rectangle(
                    dot_size*j,
                    dot_size*i,
                    dot_size*(j+1),
                    dot_size*(i+1),
                    fill=DOT_COLOR,
                    width = 0
                ),
                not bool(field[i][j])
            )
            if field[i][j]:
                canvas.create_oval(
                    dot_size*j + offset,
                    dot_size*i + offset,
                    dot_size*(j+1) - offset,
                    dot_size*(i+1) - offset,
                    fill=POINT_COLOR,
                    width = 0
                )   
            canvas.a_dots[i].append(dot_)
    return canvas

def g_h_counter(current, dot_, end):
    len_ = abs(current.i - dot_.i) + abs(current.j - dot_.j)
    added_G = 10 if len_ == 1 else pow(200, 1/2)
    G = current.G + added_G
    H = (abs(end.i - dot_.i) + abs(end.j - dot_.j)) * 10
    return G, H

def draw_line(canvas, current):
    global LINE_COLOR, DOT_SIZE
    # print(canvas.path_lines)
    # for line in canvas.path_lines:
    canvas.delete(canvas.path_line)
    # canvas.path_lines.clear()
    line_coords = []
    while True:
        coords = canvas.coords(current.id_)
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        line_coords.extend([x, y])
        current = current.parent
        if not current:
            break
    if len(line_coords) > 2:
        canvas.path_line = canvas.create_line(
                *line_coords,
                fill = LINE_COLOR,
                width = DOT_SIZE / 3
            )
    # canvas.path_lines.append(line)

    # while current.parent:
    #     coords = canvas.coords(current.id_)
    #     parent_coords = canvas.coords(current.parent.id_)
    #     # print("coords")
    #     # print(coords)
    #     # print(parent_coords)
    #     x = (parent_coords[0] + parent_coords[2]) / 2
    #     y = (parent_coords[1] + parent_coords[3]) / 2
    #     par_x = (coords[0] + coords[2]) / 2
    #     par_y = (coords[1] + coords[3]) / 2
    #     line = canvas.create_line(
    #         x,
    #         y,
    #         par_x,
    #         par_y,
    #         fill = LINE_COLOR,
    #         width = DOT_SIZE / 3
    #     )

    #     # print('ну че тут походу')
    #     # print(canvas.coords(line))
    #     canvas.path_lines.append(line)
    #     current = current.parent


def path_finder(canvas, root):
    global CLOSE_DOT_COLOR
    canvas.path_line = None
    dots = canvas.a_dots
    open_list = []
    closed_list = []
    start = dots[0][0]
    canvas.itemconfig(start.id_, fill = CLOSE_DOT_COLOR)
    current = start
    end = dots[-1][-1]
    closed_list.append(current)

    def step(root, canvas, current, dots, open_list, closed_list, end):
        global SPEED, OPEN_DOT_COLOR, CLOSE_DOT_COLOR
        for i in range(current.i-1, current.i + 2):
            for j in range(current.j-1, current.j + 2):
                if i >= 0 and j >= 0 and i < len(dots) and j < len(dots[0]):
                    if (not dots[i][j] in closed_list) and dots[i][j].available:
                        G, H = g_h_counter(current, dots[i][j], end)
                        if not ((dots[i][j] in open_list) and (dots[i][j].G <= G)):
                            dots[i][j].G = G
                            dots[i][j].H = H
                            dots[i][j].F = G + H
                            dots[i][j].parent = current
                            open_list.append(dots[i][j])
                            canvas.itemconfig(dots[i][j].id_, fill = OPEN_DOT_COLOR)
                            

        
        current = min(open_list, key = lambda dot_: dot_.F)
        open_list.remove(current)
        closed_list.append(current)
        canvas.itemconfig(current.id_, fill = CLOSE_DOT_COLOR)
#         print(f'''----------------------------------
# {current.i, current.j, current.parent.i, current.parent.j}
# {current.G, current.H, current.F}''')
        draw_line(canvas, current)
        # print('---------------------------')
        if current != end:
            root.after(SPEED, step, root, canvas, current, dots, open_list, closed_list, end)


    step(root, canvas, current, dots, open_list, closed_list, end)

def width_finder(canvas, root):
    dots = canvas.a_dots
    canvas.path_line = None
    q = Queue()
    q.put(dots[0][0])

    def step(canvas, root, dots, q):
        global SPEED, OPEN_DOT_COLOR, CLOSE_DOT_COLOR
        current = q.get()
        current.G = 1
        canvas.itemconfig(current.id_, fill = CLOSE_DOT_COLOR)
        neignbours = [
            [current.i-1, current.j],
            [current.i+1, current.j],
            [current.i, current.j-1],
            [current.i, current.j+1]
        ]
        for i, j in neignbours:
            if i >= 0 and j >= 0 and i < len(dots) and j < len(dots[0]):
                if not dots[i][j].G and not dots[i][j].H and dots[i][j].available:
                    dots[i][j].parent = current
                    q.put(dots[i][j])
                    dots[i][j].H = 1
                    canvas.itemconfig(dots[i][j].id_, fill = OPEN_DOT_COLOR)

        draw_line(canvas, current)

        if current != dots[-1][-1]:
            root.after(SPEED, step, canvas, root, dots, q)

    # root.after(5000, step, canvas, root, dots, q)
    step(canvas, root, dots, q)


root = Tk()
canvas = draw_field(root, FIELD, DOT_SIZE)
path_finder(canvas, root)


root.mainloop()