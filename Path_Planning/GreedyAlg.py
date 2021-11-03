# !/usr/bin/env python3
from tkinter import *

import tkinter as tk
import time
import math
import random

class Grid:

    def __init__(self, root, width, height, numWidth, numHeight, line_width):
        self.totalDistance = 0
        self.grid = []
        for y in range(numHeight):
            tmp = []
            for i in range(numWidth):
                tmp.append(' ')
            self.grid.append(tmp)

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

    def setEnd(self, x, y):
        self.grid[y][x] = 'e'
        self.endX = x
        self.endY = y
        self.end = self.c.create_rectangle((x*self.width/self.numWidth) + self.line_width, (y*self.height/self.numHeight) + self.line_width, ((x+1)*self.width/self.numWidth),
                                          ((y+1)*self.height/self.numHeight),
                                          fill='#eb4034', outline="")
        self.endPos = [x, y]

    def setWall(self, x, y):
        self.grid[y][x] = 'w'
        self.wall = self.c.create_rectangle((x*self.width/self.numWidth) + self.line_width, (y*self.height/self.numHeight) + self.line_width, ((x+1)*self.width/self.numWidth),
                                          ((y+1)*self.height/self.numHeight),
                                          fill='#787878', outline="")

    def setLocation(self, x, y):
        self.grid[y][x] = 'l'
        self.location = self.c.create_rectangle((x*self.width/self.numWidth) + self.line_width, (y*self.height/self.numHeight) + self.line_width, ((x+1)*self.width/self.numWidth),
                                          ((y+1)*self.height/self.numHeight),
                                          fill='#fff200', outline="")
        print("LOCATION: ", x, y)

    def getDistance(self, x1, y1, x2, y2):
        return math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )

    def getMin(self, arr):
        min = 0
        for i in range(len(arr)):
            if(arr[i][0] < arr[min][0]):
                min = i
        return min

    def findPath(self):
        curX, curY = self.startX, self.startY
        while(not(curX == self.endX and curY == self.endY)):
            dist = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (not (i == 0 and j == 0) and curX + j >= 0 and curY + i >= 0 and curX + j < self.numWidth and curY + i < self.numHeight and
                            (self.grid[curY + i][curX + j] == ' ' or self.grid[curY + i][curX + j] == 'e')):
                        dist.append([self.getDistance(curX + j, curY + i, self.endX, self.endY), curX + j, curY + i])
            min = dist[self.getMin(dist)]
            self.totalDistance += 1
            curX = min[1]
            curY = min[2]
            self.setLocation(curX, curY)
            time.sleep(0.01)
            win.update()
        print("DONE", "Distance = ", self.totalDistance)


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
width = 800
height = 800
line_width = 1
dim = str(width+line_width) + "x" + str(height+line_width)

win = tk.Tk()
win.title("Gauge ELement")
win.geometry(dim)
win.configure(bg='black')

g = Grid(win, width, height, 100, 100, line_width)
g.setStart(0, 0)
g.setEnd(90, 47)
for i in range(50):
    g.setWall(10, i)

for i in range(30):
    g.setWall(40, i)
g.getWidget().pack()

g.findPath()
win.mainloop()