from random import randrange
from tkinter import *
import math
import tkinter as tk
import time

class node:
	def __init__(self, number, x, y, g, h, parent):
		self.number = number
		self.x = x
		self.y = y
		self.g = g
		self.h = h
		self.f = g + h
		self.parent = parent

'''
class Grid:

    def __init__(self, root, width, height, numWidth, numHeight, line_width):
        self.totalDistance = 0
        self.grid = []
        self.visited = []
        for y in range(numHeight):
            tmp = []
            tmpV = []
            for i in range(numWidth):
                tmp.append(' ')
                tmpV.append(0)
            self.grid.append(tmp)
            self.visited.append(tmpV)

        self.root = root
        self.width = width
        self.height = height
        self.numWidth = numWidth
        self.numHeight = numHeight
        self.line_width = line_width

        self.c = Canvas(root, width=width+1, height=height+1, bg="black", highlightthickness=0)
        for i in range(numWidth+1):
            xy = [(i * width / numWidth, 0), (i * width / numWidth, height)]
            self.c.create_line(xy, width=line_width, fill='white')
        for i in range(numHeight+1):
            xy = [(0, i * height / numHeight), (width, i * height / numHeight)]
            self.c.create_line(xy, width=line_width, fill='white')

    def setStart(self, x, y):
        self.grid[y][x] = 's'
        self.startX = x
        self.startY = y
        self.start = self.c.create_rectangle((x * self.width / self.numWidth) + self.line_width,
                                             (y * self.height / self.numHeight) + self.line_width,
                                             ((x + 1) * self.width / self.numWidth),
                                             ((y + 1) * self.height / self.numHeight),
                                             fill='#41d94d', outline="")
        self.startPos = [x, y]
        self.visited[y][x] = 1

        self.prvX, self.prvY = x, y


    def setWall(self, x, y):
        self.grid[y][x] = 'w'
        self.wall = self.c.create_rectangle((x*self.width/self.numWidth) + self.line_width, (y*self.height/self.numHeight) + self.line_width, ((x+1)*self.width/self.numWidth),
                                          ((y+1)*self.height/self.numHeight),
                                          fill='#787878', outline="")

    def setLocation(self, x, y):
        self.grid[y][x] = 'l'
        self.visited[y][x] = 1
        self.location = self.c.create_rectangle((x*self.width/self.numWidth) + self.line_width, (y*self.height/self.numHeight) + self.line_width, ((x+1)*self.width/self.numWidth),
                                          ((y+1)*self.height/self.numHeight),
                                          fill='white', outline="")
        xy = [((self.prvX*self.width/self.numWidth) + (self.width/self.numWidth)/2, (self.prvY*self.height/self.numHeight) + (self.height/self.numHeight)/2), ((x*self.width/self.numWidth) + (self.width/self.numWidth)/2, (y*self.height/self.numHeight) + (self.height/self.numHeight)/2) ]
        self.line = self.c.create_line(xy, width=3, fill='red')
        self.totalDistance += math.sqrt(math.pow(y - self.prvY, 2) + math.pow(x - self.prvX, 2))
        self.prvX = x
        self.prvY = y
        print("LOCATION: ", x, y)

    def pathAvailable(self, x, y):
        if (x + 1 < self.numWidth and not self.visited[y][x + 1] and self.grid[y][x+1] != 'w'):
            return True
        if (x - 1 >= 0 and not self.visited[y][x - 1] and self.grid[y][x-1] != 'w'):
            return True
        if (y + 1 < self.numHeight and not self.visited[y + 1][x] and self.grid[y+1][x] != 'w'):
            return True
        if (y - 1 >= 0 and not self.visited[y - 1][x] and self.grid[y-1][x] != 'w'):
            return True
        return False

    def printFreeSpaces(self, x, y):
        if (x + 1 < self.numWidth and not self.visited[y][x + 1] and self.grid[y][x+1] != 'w'):
            print('2')
        elif (x - 1 >= 0 and not self.visited[y][x - 1] and self.grid[y][x-1] != 'w'):
            print('4')
        elif (y + 1 < self.numHeight and not self.visited[y + 1][x] and self.grid[y+1][x] != 'w'):
            print('1')
        elif (y - 1 >= 0 and not self.visited[y - 1][x] and self.grid[y-1][x] != 'w'):
            print('3')
        else:
            print("no paths")


    def coveragePath(self):
        dirSwap = True
        curX, curY = 0, 0
        first = False
        stack = []
        #stack = [[curX, curY, dirSwap]]  # full of visited points

        #print("LOOP: " + str(not (curX == self.startX and curY == self.startY) or not first))

        while(not(curX == self.startX and curY == self.startY) or not first):
            first = True
            if(curX < self.numWidth and curY < self.numHeight and not self.pathAvailable(curX, curY) and len(stack) > 1):
                #backtrack
                while(not self.pathAvailable(curX, curY) and len(stack) > 1):
                    stack.pop()
                    curX = stack[len(stack)-1][0]
                    curY = stack[len(stack)-1][1]
                    dirSwap = stack[len(stack)-1][2]
                    print("BACKTRACK", curX, curY)
            else:
                stack.append([curX, curY, dirSwap])
                if (curX + 1 < self.numWidth and self.grid[curY][curX + 1] != 'w' and not self.visited[curY][curX+1]):
                    curX += 1
                    self.visited[curY][curX] = 1
                elif (curX - 1 >= 0 and self.grid[curY][curX - 1] != 'w' and not self.visited[curY][curX-1]):
                    curX -= 1
                    self.visited[curY][curX] = 1
                elif (curY + 1 < self.numHeight and self.grid[curY + 1][curX] != 'w' and not self.visited[curY + 1][curX]):
                    curY += 1
                    self.visited[curY][curX] = 1
                elif (curY - 1 >= 0 and self.grid[curY - 1][curX] != 'w' and not self.visited[curY - 1][curX]):
                    curY -= 1
                    self.visited[curY][curX] = 1
            #print("VISIT STATE: ", self.visited[curY][curX])
            self.setLocation(curX, curY)
            #time.sleep(0.1)
            win.update()
        print("DONE", "total distance =", self.totalDistance)


    def printGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if(self.grid[i][j] == ' '):
                    print('-', end="")
                else:
                    print(self.grid[i][j], end="")
            print()



    def getWidget(self):
        return self.c

'''

counter = 0
gridX = 20
gridY = 20
coordX = 0
coordY = 0
#startX = randrange(gridX)
#startY = randrange(gridY)
startX = 1
startY = 1
#goalX = randrange(gridX)
#goalY = randrange(gridY)
goalX = 4
goalY = 5
print("Goal: "  + str(goalX) + ", "+ str(goalY))

coordinates = []
explored = []
exploredNodes = []
nodes = []
path = []
obstacles = [(3,3), (3,4), (3, 5), (4, 3)]

#coordinates.append((startX, startY))
#coordinates.append((goalX, goalY))

def calculateH(x, y):
	h = 0
	while x != goalX or y != goalY:
		if x == goalX and y < goalY:
			y = y + 1
			h = h + 1
		if x == goalX and y > goalY:
			y = y - 1
			h = h + 1
		if x > goalX and y == goalY:
			x = x - 1
			h = h + 1
		if x < goalX and y == goalY:
			x = x + 1
			h = h + 1
		if x < goalX and y < goalY:
			x = x + 1
			y = y + 1
			h = h + 1.4
		if x > goalX and y > goalY:
			x = x - 1
			y = y - 1
			h = h + 1.4
		if x > goalX and y < goalY:
			x = x - 1
			y = y + 1
			h = h + 1.4
		if x < goalX and y > goalY:
			x = x + 1
			y = y - 1
			h = h + 1.4
	return h

start = node(counter, startX, startY, 0, calculateH(startX, startY), counter)
nodes.append(start)
coordinates.append((startX, startY, calculateH(startX, startY)))
counter += 1

goal = node(counter, goalX, goalY, 0, calculateH(startX, startY),counter)
counter += 1

def checkNeighbors(parentNode):
	global counter
	#print("parentNode G: " + str(parentNode.g))
	'''
	if (parentNode.x + 1, parentNode.y) in explored:
		for node in exploredNodes:
			if node.x == parentNode.x + 1 and node.y == parentNode.y:
				if node.g > parentNode.g + 1:
					node.g = parentNode.g
					node.parent = parentNode.counter
			break
	'''

	if (parentNode.x + 1, parentNode.y, parentNode.g + 1 + calculateH(parentNode.x + 1, parentNode.y)) not in coordinates and (parentNode.x + 1, parentNode.y) not in explored and (parentNode.x + 1, parentNode.y) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y > 0 and parentNode.y <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y, parentNode.g + 1, calculateH(parentNode.x + 1, parentNode.y), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y, parentNode.g + 1 + calculateH(parentNode.x + 1, parentNode.y)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x + 1, parentNode.y + 1, parentNode.g + 1.4 + calculateH(parentNode.x + 1, parentNode.y + 1)) not in coordinates and (parentNode.x + 1, parentNode.y + 1) not in explored and (parentNode.x + 1, parentNode.y + 1) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y + 1, parentNode.g + 1.4, calculateH(parentNode.x + 1, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y + 1, 1.4 + calculateH(parentNode.x + 1, parentNode.y + 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))		
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x, parentNode.y + 1, parentNode.g + 1 + calculateH(parentNode.x, parentNode.y + 1)) not in coordinates and (parentNode.x, parentNode.y + 1) not in explored and (parentNode.x, parentNode.y + 1) not in obstacles and parentNode.x > 0 and parentNode.x <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x, parentNode.y + 1, parentNode.g + 1, calculateH(parentNode.x, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x, parentNode.y + 1, parentNode.g + 1 + calculateH(parentNode.x, parentNode.y + 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x - 1, parentNode.y + 1, parentNode.g + 1.4 + calculateH(parentNode.x - 1, parentNode.y + 1)) not in coordinates and (parentNode.x - 1, parentNode.y + 1) not in explored and (parentNode.x - 1, parentNode.y + 1) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y + 1, parentNode.g + 1.4, calculateH(parentNode.x - 1, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y + 1, parentNode.g + 1.4 + calculateH(parentNode.x - 1, parentNode.y + 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x - 1, parentNode.y, parentNode.g + 1 + calculateH(parentNode.x - 1, parentNode.y)) not in coordinates and (parentNode.x - 1, parentNode.y) not in explored and (parentNode.x - 1, parentNode.y) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y > 0 and parentNode.y <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y, parentNode.g + 1, calculateH(parentNode.x - 1, parentNode.y), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y, parentNode.g + 1 + calculateH(parentNode.x - 1, parentNode.y)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x - 1, parentNode.y - 1, parentNode.g + 1.4 + calculateH(parentNode.x - 1, parentNode.y - 1)) not in coordinates and (parentNode.x - 1, parentNode.y - 1) not in explored and (parentNode.x - 1, parentNode.y - 1) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y - 1, parentNode.g + 1.4, calculateH(parentNode.x - 1, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y - 1, 1.4 + calculateH(parentNode.x - 1, parentNode.y - 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if (parentNode.x, parentNode.y - 1, parentNode.g + 1 + calculateH(parentNode.x, parentNode.y - 1)) not in coordinates and (parentNode.x, parentNode.y - 1) not in explored and (parentNode.x, parentNode.y - 1) not in obstacles and parentNode.x > 0 and parentNode.x <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x, parentNode.y - 1, parentNode.g + 1, calculateH(parentNode.x, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x, parentNode.y - 1, parentNode.g + 1 + calculateH(parentNode.x, parentNode.y - 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

	if  (parentNode.x + 1, parentNode.y - 1, parentNode.g + 1.4 + calculateH(parentNode.x + 1, parentNode.y - 1)) not in coordinates and (parentNode.x + 1, parentNode.y - 1) not in explored and (parentNode.x + 1, parentNode.y - 1) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y - 1, parentNode.g + 1.4, calculateH(parentNode.x + 1, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y - 1, 1.4 + calculateH(parentNode.x + 1, parentNode.y - 1)))
		counter += 1
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)
		coordinates.sort(key = lambda x: x[2], reverse = True)

while goal not in coordinates:
	current = nodes[len(nodes) - 1]
	currentCoordinate = coordinates[len(coordinates) - 1]
	#print("checking " + str(current.x) + ", "+ str(current.y) + " F: " + str(current.f))
	print("checking: " + str(current.x) + ", " + str(current.y) + " number: " + str(current.number) + " parent: " + str(current.parent))
	exploredNodes.append(current)
	nodes.remove(nodes[len(nodes) - 1])
	explored.append((current.x, current.y))
	coordinates.remove(coordinates[len(coordinates) - 1])
	if (current.x, current.y) == (goal.x, goal.y):
		break
	else:
		checkNeighbors(current)
'''
print("explored")
for x in exploredNodes:
	print("number: " + str(x.number) + " " + str(x.x) + ", " + str(x.y) + " parent: " + str(x.parent))
'''
for x in path:
	print(str(x.x) + ", " + str(x.y))

for node in exploredNodes:
	if node.x == goalX and node.y == goalY:
		print("added goal to path") 
		path.append(node)
		break

for x in path:
	print(str(x.x) + ", " + str(x.y))

print("creating path")

while path[len(path) - 1].parent != 0:
	curent = path[len(path) - 1]
	for node in exploredNodes:
		#print("number: " + str(node.number))
		if node.number == current.parent:
			path.append(node)
			#print("Adding: " + str(node.x) + ", " + str(node.y))
			print("adding to path " + str(node.x) + ", " + str(node.y) + " number: " + str(node.number) + " parent: " + str(node.parent))
			current = node
			break
path.append(start)

print("Start: "  + str(startX) + ", "+ str(startY))
print("Goal: "  + str(goalX) + ", "+ str(goalY))

for x in path:
	print(str(x.x) + ", " + str(x.y))

'''
for x in coordinates:
	print(str(x[0]) + ", " + str(x[1]))
'''
'''
win = tk.Tk()
win.title("Complete Cov")
win.geometry(dim)
win.configure(bg='black')
g = Grid(win, width, height, 100, 100, line_width)
g.setStart(0, 0)
for i in range(50):
    g.setWall(10, i)
 
for i in range(50):
    g.setWall(40, i)

g.setWall(50, 50)
g.setWall(50, 51)
g.setWall(51, 50)
g.setWall(51, 51)

g.setWall(78, 78)
g.setWall(78, 79)
g.setWall(79, 78)
g.setWall(79, 79)

for i in range(5):
    for j in range(5):
        g.setWall(20+i, 80+j)

for i in range(5):
    for j in range(5):
        g.setWall(20+i, 30+j)


g.getWidget().pack()

g.coveragePath()
win.mainloop()
'''