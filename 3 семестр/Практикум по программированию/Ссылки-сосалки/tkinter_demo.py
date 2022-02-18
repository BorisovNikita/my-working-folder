from tkinter import *
from random import *
from math import *
import time

# Создаем окно программы
root = Tk()
# Создаем область для рисования
c = Canvas(root, width=600, height=600, bg="white")
c.pack()

# Для движущейся точки создадим класс
class Dot:
	def __init__(self, canvas, center, dist):
		self.angle = 0		# текущий угол
		self.radius = 10	# радиус кружка
		self.canvas = canvas    # ссылка на рисовалку для удобства
		self.center = center	# центр окружности
		self.dist = dist	# расстояние до центра
		self.x, self.y = self.p2c()	# преобразуем угол в координаты. 
		# Рисуем начальное положение
		self.shape = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill='red')
		# Запускаем анимацию
		self.update()

	def update(self):
		# Вычисляем новые координаты
		new = self.p2c()
		# Двигаем кружок на дельту
		self.canvas.move(self.shape, new[0]-self.x, new[1]-self.y)
		# Сохраняем новые кординаты как текущие
		(self.x, self.y) = new
		# Через 15мс (примерно соответствует 60 кадрам в сек) повторяем
		self.canvas.after(15, self.update)
		# Увеличиваем угол
		self.angle += 0.03

	# Это по сути преобразование от полярных к декартовым.
	def p2c(self):
		return cos(self.angle) * self.dist + self.center[0], sin(self.angle) * self.dist + self.center[1]

# Статичные элементы рисовать легко
c.create_oval(100, 100, 500, 500)

# Содаем экземпляр точки
dot = Dot(c, (300, 300), 200)

# Запускаем главный цикл
root.mainloop()