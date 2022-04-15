# !/usr/bin/env python3
from tkinter import *

import tkinter as tk
import time
import math

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
        #print("LOCATION: ", x, y)

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
                    #print("BACKTRACK", curX, curY)
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




#GAUGE TEST CODE
width = 400
height = 400
x = 0
y = 0
line_width = 1
dim = str(width+line_width) + "x" + str(height+line_width)

win = tk.Tk()
win.title("Complete Cov")
win.geometry(dim)
win.configure(bg='black')
g = Grid(win, width, height, 200, 200, line_width)

f = open("fatJigglyAss.txt", "r")
walls = f.read()

walls = walls.split(",")

start = walls[0].strip("[")
start = start.strip("]")

for number in range(len(start)):
    if start[number] == " ":
        split = number

startX = int(start[0: split])
startY = int(start[split: -1])

walls.pop(0)

g.setStart(startX,startY)

walls.pop(0)

for wall in walls:
    x = 0
    for point in wall:
        if int(point) == 1:
            g.setWall(y, x)
        x = x + 1
    y = y + 1

g.getWidget().pack()

g.coveragePath()
win.mainloop()
