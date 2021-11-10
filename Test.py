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

counter = 0
gridX = 10
gridY = 10
#coordX = 0
#coordY = 0
startX = randrange(gridX) + 1
startY = randrange(gridY) + 1
#startX = 1
#startY = 1
goalX = randrange(gridX) + 1
goalY = randrange(gridY) + 1
#oalX = 6
#goalY = 3
print("Goal: "  + str(goalX) + ", "+ str(goalY))

coordinates = []
explored = []
exploredNodes = []
nodes = []
path = []
#obstacles = [(3,3), (4,3), (4,2)]
obstacles = [(2,3), (2,4), (2,5), (2,6), (2, 7), (2, 8), (3,6), (4,6), (5,6), (6,6), (7,6), (7,7), (7,8), (7,9), (4,2), (4,3), (6,2), (7,2), (8,2), (9,2), (9,3), (9,4), (9, 5)]

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
coordinates.append((startX, startY))
counter += 1

goal = node(counter, goalX, goalY, 0, calculateH(startX, startY),counter)
print(node)
counter += 1

def checkNeighbors(parentNode):
	global counter
	#print("parentNode G: " + str(parentNode.g))
	print(coordinates)
	print("Parent: "+ str(parentNode.x) + ", " + str(parentNode.y))
	if (parentNode.x + 1, parentNode.y) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x + 1 and ex.y == parentNode.y:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x + 1, parentNode.y)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x + 1, parentNode.y) not in explored and (parentNode.x + 1, parentNode.y) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y > 0 and parentNode.y <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y, parentNode.g + 1, calculateH(parentNode.x + 1, parentNode.y), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x + 1, parentNode.y + 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x + 1 and ex.y == parentNode.y + 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x + 1, parentNode.y + 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x + 1, parentNode.y + 1) not in explored and (parentNode.x + 1, parentNode.y + 1) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y + 1, parentNode.g + 1.4, calculateH(parentNode.x + 1, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y + 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))		
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x, parentNode.y + 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x and ex.y == parentNode.y + 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x, parentNode.y + 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x, parentNode.y + 1) not in explored and (parentNode.x, parentNode.y + 1) not in obstacles and parentNode.x > 0 and parentNode.x <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x, parentNode.y + 1, parentNode.g + 1, calculateH(parentNode.x, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x, parentNode.y + 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x - 1, parentNode.y + 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x - 1 and ex.y == parentNode.y + 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x - 1, parentNode.y + 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x - 1, parentNode.y + 1) not in explored and (parentNode.x - 1, parentNode.y + 1) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y + 1 > 0 and parentNode.y + 1 <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y + 1, parentNode.g + 1.4, calculateH(parentNode.x - 1, parentNode.y + 1), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y + 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x - 1, parentNode.y) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x - 1 and ex.y == parentNode.y:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x - 1, parentNode.y)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	if (parentNode.x - 1, parentNode.y) not in coordinates and (parentNode.x - 1, parentNode.y) not in explored and (parentNode.x - 1, parentNode.y) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y > 0 and parentNode.y <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y, parentNode.g + 1, calculateH(parentNode.x - 1, parentNode.y), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x - 1, parentNode.y - 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x - 1 and ex.y == parentNode.y - 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x - 1, parentNode.y - 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x - 1, parentNode.y - 1) not in explored and (parentNode.x - 1, parentNode.y - 1) not in obstacles and parentNode.x - 1 > 0 and parentNode.x - 1 <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x - 1, parentNode.y - 1, parentNode.g + 1.4, calculateH(parentNode.x - 1, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x - 1, parentNode.y - 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x, parentNode.y - 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x and ex.y == parentNode.y - 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x, parentNode.y - 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif (parentNode.x, parentNode.y - 1) not in explored and (parentNode.x, parentNode.y - 1) not in obstacles and parentNode.x > 0 and parentNode.x <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x, parentNode.y - 1, parentNode.g + 1, calculateH(parentNode.x, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x, parentNode.y - 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

	if (parentNode.x + 1, parentNode.y - 1) in coordinates:
		print("Changing G value")
		for ex in nodes:
			if ex.x == parentNode.x + 1 and ex.y == parentNode.y - 1:
				if ex.g > parentNode.g + 1:
					ex.g = parentNode.g + 1
					ex.f = ex.g + calculateH(parentNode.x + 1, parentNode.y - 1)
					ex.parent = parentNode.number
					nodes.sort(key = lambda x: x.f, reverse = True)
				break

	elif  (parentNode.x + 1, parentNode.y - 1) not in explored and (parentNode.x + 1, parentNode.y - 1) not in obstacles and parentNode.x + 1 > 0 and parentNode.x + 1 <= gridX and parentNode.y - 1 > 0 and parentNode.y - 1 <= gridY:
		nodes.append(node(counter, parentNode.x + 1, parentNode.y - 1, parentNode.g + 1.4, calculateH(parentNode.x + 1, parentNode.y - 1), parentNode.number))
		coordinates.append((parentNode.x + 1, parentNode.y - 1))
		counter += 1
		print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y))
		#print("adding " + str(nodes[len(nodes) - 1].x) + ", " + str(nodes[len(nodes) - 1].y) + " g: " + str(nodes[len(nodes) - 1].g) + " h: " + str(nodes[len(nodes) - 1].h) + " f: " + str(nodes[len(nodes) - 1].f))
		nodes.sort(key = lambda x: x.f, reverse = True)

while goal not in nodes:
	current = nodes[len(nodes) - 1]
	#print("checking " + str(current.x) + ", "+ str(current.y) + " F: " + str(current.f))
	print("checking: " + str(current.x) + ", " + str(current.y) + " number: " + str(current.number) + " parent: " + str(current.parent))
	exploredNodes.append(current)
	explored.append((current.x, current.y))
	nodes.remove(nodes[len(nodes) - 1])
	coordinates.remove((current.x, current.y))
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
	current = path[len(path) - 1]
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
