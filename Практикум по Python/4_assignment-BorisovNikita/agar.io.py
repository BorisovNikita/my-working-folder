from tkinter import Tk, Canvas, ALL
from random import randint
from math import pi


class Agar():

    def __init__(self, field, r = 8):
        self.field = field
        self.r = r
        self.weight = pi * r**2
        self.x = self.y = self.field.size / 2
        self.id = self.field.canvas.create_oval(
            self.x - r,
            self.y - r,
            self.x + r,
            self.y + r,
            fill = "#000080",
            width = 2,
            outline = '#008000'
        )

    def move(self, speed):
        self.x = self.field.center_x - self.field.offset[0]
        self.y = self.field.center_y - self.field.offset[1]

    def eat(self, dot):
        self.weight += pi * dot.r**2
        ratio = self.field.ratio
        self.r = (self.weight / pi)**(1/2)
        self.r = self.r if self.r < self.field.max_r else self.field.max_r
        x = self.field.center_x
        y = self.field.center_y
        self.field.canvas.coords(
            self.id,
            x - self.r * ratio,
            y - self.r * ratio,
            x + self.r * ratio,
            y + self.r * ratio,
        )


class Dot(object):

    def __init__(self, field,r = 5, fill = "white"):
        self.field = field
        self.r = r
        self.x, self.y = self.rand_x_y()
        self.id = self.field.canvas.create_oval(
            *self.x_y(),
            fill=fill,
            outline="#008000",
            width=2
        )
        self.change_color()

    def change_color(self):
        i = randint(0, len(self.field.colors)-1)
        j = randint(0, len(self.field.colors)-1)
        self.field.canvas.itemconfig(
            self.id,
            fill=self.field.colors[i],
            outline=self.field.colors[j]
        )

    def rand_x_y(self):
        x = randint(0 + self.r, self.field.size - self.r)
        y = randint(0 + self.r, self.field.size - self.r)
        return x,y

    def x_y(self):
        field = self.field
        agar = field.agars[0]
        ratio = field.ratio
        agar.x, agar.y
        x = (self.x - agar.x) * ratio + field.center_x
        y = (self.y - agar.y) * ratio + field.center_y
        r = self.r * ratio
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return x0, y0, x1, y1

    def redraw(self):
        self.field.canvas.coords(
            self.id, 
            *self.x_y()
        )

    def reborn(self):
        self.x, self.y = self.rand_x_y()
        self.change_color()
        for agar in self.field.agars:
            vector = [self.x - agar.x, self.y - agar.y]
            distance = self.field.vec_len(vector)
            if (self.r + agar.r) >=distance:
                self.reborn()
                break
        else:
            self.redraw()


class Border(object):

    def __init__(self, field, width):
        self.field = field
        self.width = width
        self.min = 0 
        self.max = self.field.size
        self.id = self.field.canvas.create_line(
            *self.coords(),
            width=width,
            fill = 'red'
        )

    def coords(self):
        field = self.field
        ratio = field.ratio
        agar = self.field.agars[0]
        x0_agar, y0_agar = agar.x, agar.y
        x0_canv, y0_canv = field.center_x, field.center_y
        x1 = (self.min - x0_agar) * ratio + x0_canv - (self.width // 2 + 1)
        y1 = (self.min - y0_agar) * ratio + y0_canv - (self.width // 2 + 1)
        x2 = (self.max - x0_agar) * ratio + x0_canv + (self.width // 2 + 1)
        y2 = (self.max - y0_agar) * ratio + y0_canv + (self.width // 2 + 1)
        line_dots = [
            x1, y1,
            x2, y1,
            x2, y2,
            x1, y2,
            x1, y1,
        ]
        return line_dots

    def redraw(self):
        self.field.canvas.coords(
            self.id,
            *self.coords()
        )
        

class Field(object):
    
    def __init__(self, size = 1000, w_width = 600, w_height = 600, max_r = None, dot_count = None):
        self.size = size
        self.dot_count = int(size / 10) if not dot_count else dot_count
        self.w_width = w_width
        self.w_height = w_height
        self.center_x = w_width / 2
        self.center_y = w_height / 2
        self.offset = [0, 0]
        self.mouse_x = w_width / 2
        self.mouse_y = w_height / 2
        self.max_speed = 5
        self.min_speed = 2
        self.max_r = size / 10 if not max_r else max_r
        self.min_r = 8
        self.ratio = 1
        self.limiter = 0.05
        self.gen_colors()

    def gen_colors(self):
        self.colors = []
        for i in range(0x0, 0xFF, 0x8):
            col1 = f'#{i:0>2x}{(255-i):0>2x}00'
            col2 = f'#00{i:0>2x}{(255-i):0>2x}'
            col3 = f'#{(255-i):0>2x}00{i:0>2x}'
            self.colors.extend([col1, col2, col3])

    def canvas_init(self):
        self.root = Tk()
        self.canvas = Canvas(
            self.root,
            width=self.w_width,
            height=self.w_height,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

    def dots_init(self):
        self.dots = []
        for _ in range(self.dot_count):
            self.dots.append(
                Dot(self)
            )

    def agars_init(self):
        self.agars = []
        self.agars.append(Agar(self, self.min_r))
    
    def border_init(self, width = 11):
        self.border = Border(self, width)
    
    def focus_on(self):
        offset = [
            self.center_x - self.agars[0].x,
            self.center_y - self.agars[0].y
        ]
        self.offset[0] += offset[0]
        self.offset[1] += offset[1]
        self.border.redraw()
        for dot in self.dots:
            dot.redraw()
        r = self.agars[0].r
        id_ = self.agars[0].id
        self.canvas.coords(
            id_,
            self.center_x - r,
            self.center_y - r,
            self.center_x + r,
            self.center_y + r
        )

    def move(self, speed):
        self.offset[0] += speed[0]
        self.offset[1] += speed[1]
        self.agars[0].move(speed)
        for dot in self.dots:
            dot.redraw()

        self.border.redraw()

    def vec_len(self, vector):
        return (vector[0]**2 + vector[1]**2)**(1/2)

    def normalize(self, vector):
        len_ = self.vec_len(vector)
        if not len_:
            return vector
        vector[0] /= len_
        vector[1] /= len_
        return vector

    def truncate(self, vector, r, cur_r):
        ratio = cur_r / r
        ratio = ratio if ratio < 1.0 else 1
        vector[0] *= ratio
        vector[1] *= ratio
        return vector
    
    def restrict(self, speed):
        x, y = self.agars[0].x, self.agars[0].y
        r = self.agars[0].r
        allow_x = x - r
        if allow_x - speed[0] < 0:
            speed[0] = allow_x
        allow_y = y - r
        if allow_y - speed[1] < 0:
            speed[1] = allow_y
        allow_x = x + r
        if allow_x - speed[0] > self.size:
            speed[0] = allow_x - self.size
        allow_y = y + r
        if allow_y - speed[1] > self.size:
            speed[1] = allow_y - self.size
        return speed

    def speed(self):
        r = self.agars[0].r
        speed_vector = [self.center_x - self.mouse_x, self.center_y - self.mouse_y]
        distance = self.vec_len(speed_vector) / self.ratio
        self.normalize(speed_vector)
        speed = self.max_speed - (self.max_speed - self.min_speed) * ((self.agars[0].r - self.min_r) / (self.max_r - self.min_r))
        speed_vector[0] *= speed
        speed_vector[1] *= speed
        self.truncate(speed_vector, r, distance)
        self.restrict(speed_vector)
        return speed_vector

    def update_mouse(self):
        mouse_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        mouse_y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        if 0 <= mouse_x <= self.w_width and 0 <= mouse_y <= self.w_height:
            self.mouse_x = mouse_x
            self.mouse_y = mouse_y

    def eating(self):
        for dot in self.dots:
            agar = self.agars[0]
            vector = dot.x - agar.x, dot.y - agar.y
            distance = self.vec_len(vector)
            if (agar.r + dot.r) >= distance:
                agar.eat(dot)
                dot.reborn()
                ratio = agar.r / self.min_r
                self.ratio = 1 / (1 + ((ratio - 1) * self.limiter))

    def motion(self):
        self.update_mouse()
        speed = self.speed()
        self.move(speed)
        self.eating()
        self.root.after(1, self.motion)
        
    def start(self):
        self.canvas_init()
        self.agars_init()
        self.border_init()
        self.dots_init()
        self.focus_on()
        # self.root.after(5000, self.motion)
        self.motion()
        self.root.mainloop()
 
field = Field(10000, 800, 800, 2500, 5000)
field.start()