from numpy import random 
from time import sleep
from os import system

MAX_ROW = 40
MAX_COL = 80
TIME_DELAY = 0.01
PROB = 0.000001


class cell(object):

	def __init__(self, alive, row, col):
		self.alive = alive
		self.row = row
		self.col = col
		self.temp_alive = alive

	def isAlive(self):
		return self.alive

	def kill(self):
		self.temp_alive = False

	def revive(self):
		self.temp_alive = True

	def nextGen(self):
		self.alive = self.temp_alive

	def chaos(self, prob):
		if random.rand() < prob:
			self.temp_alive = not self.temp_alive


class game(object):

	def __init__(self, cells, rows, cols):
		self.cells = cells
		self.rows = rows
		self.cols = cols

	def countNeighbours(self, row, col):
		count = 0
		for i in range(-1, 2):
			if row + i >= self.rows:
				i = 0 - row
			for j in range(-1, 2):
				if col + j >= self.cols:
					j = 0 - col
				if self.cells[row+i][col+j].isAlive():
					count += 1
		return count

	def nextGen(self):
		for i in range(self.rows):
			for j in range(self.cols):
				cell = self.cells[i][j]
				count = self.countNeighbours(i, j)
				if count < 3 or count > 4:
					cell.kill()
				elif count == 3:
					cell.revive()
				cell.chaos(PROB)

		for i in range(self.rows):
			for j in range(self.cols):
				self.cells[i][j].nextGen()

	def display(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.cells[i][j].isAlive():
					print("o", end=" ")
				else:
					print(" ", end=" ")
			print('\n', end="")



state = random.randint(2, size=(MAX_ROW, MAX_COL))
cells = []
for x in range(0, MAX_ROW):
	cells.append([])
	for y in range(0, MAX_COL):
		cells[x].append(cell(state[x][y], x, y))
firstTry = game(cells, MAX_ROW, MAX_COL)

while True:
	system('cls')
	firstTry.display()
	firstTry.nextGen()
	sleep(TIME_DELAY)