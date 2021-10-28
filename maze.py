import random as r
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class node:
    def __init__(self, x, y):
        self.north = 1
        self.south = 1
        self.east = 1
        self.west = 1
        self.x = x
        self.y = y

class solverNode:
    def __init__(self, steps, parent, x, y):
        self.steps = steps
        self.parent = parent
        self.x = x
        self.y = y
        
gridSize = 30
        
mapping = []
for x in range(0,gridSize):
    row = []
    for y in range(0,gridSize):
        row.append(node(x,y))
    mapping.append(row)

stack = []
visited = []

stack.append(mapping[0][0])

while len(stack) != 0:
    current = stack.pop()
    listOfPos = []
    if current.x == 0 and current.y == 0:
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x+1][current.y])
    elif current.x == gridSize-1 and current.y == gridSize-1:
        listOfPos.append(mapping[current.x-1][current.y])
        listOfPos.append(mapping[current.x][current.y-1])
    elif current.x == 0 and current.y == gridSize-1:
        listOfPos.append(mapping[current.x+1][current.y])
        listOfPos.append(mapping[current.x][current.y-1])
    elif current.x == gridSize-1 and current.y == 0:
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x-1][current.y])
    elif current.x == 0:
        listOfPos.append(mapping[current.x][current.y-1])
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x+1][current.y])
    elif current.x == gridSize-1:
        listOfPos.append(mapping[current.x][current.y-1])
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x-1][current.y])
    elif current.y == 0:
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x-1][current.y])
        listOfPos.append(mapping[current.x+1][current.y])
    elif current.y == gridSize-1:
        listOfPos.append(mapping[current.x][current.y-1])
        listOfPos.append(mapping[current.x-1][current.y])
        listOfPos.append(mapping[current.x+1][current.y])
    else:
        listOfPos.append(mapping[current.x][current.y-1])
        listOfPos.append(mapping[current.x][current.y+1])
        listOfPos.append(mapping[current.x-1][current.y])
        listOfPos.append(mapping[current.x+1][current.y])
    visited.append(current)
    r.shuffle(listOfPos)
    for n in listOfPos:
        if n in visited or n in stack:
            continue
        else:
            stack.append(n)
            if n.x < current.x:
                n.east = 0
                current.west = 0
            if n.x > current.x:
                n.west = 0
                current.east = 0
            if n.y < current.y:
                n.south = 0
                current.north = 0
            if n.y > current.y:
                n.north = 0
                current.south = 0
            
fig = plt.figure(figsize=(8,8), dpi=100)


for x in mapping:
    for y in x:
        if y.south == 1:
            xdata = [y.x, y.x+1]
            ydata = [y.y+1, y.y+1]
            plt.plot(xdata, ydata, color = 'black', linewidth=2)
        if y.north == 1:
            xdata = [y.x, y.x+1]
            ydata = [y.y, y.y]
            plt.plot(xdata, ydata, color = 'black', linewidth=2)
        if y.east == 1:
            xdata = [y.x+1, y.x+1]
            ydata = [y.y, y.y+1]
            plt.plot(xdata, ydata, color = 'black', linewidth=2)
        if y.west == 1:
            xdata = [y.x, y.x]
            ydata = [y.y, y.y+1]
            plt.plot(xdata, ydata, color = 'black', linewidth=2)
            
bfs = []
visitedbfs = []
beststeps = gridSize * gridSize
currentSol = None

bfs.append(solverNode(1, None, 0, gridSize-1))

while len(bfs) != 0:
    current = bfs.pop(0)
    coords = [current.x, current.y]
    visitedbfs.append(coords)
    if current.x == gridSize-1 and current.y == 0:
        if current.steps < beststeps:
            currentSol = current
    if mapping[current.x][current.y].north == 0 and [current.x, current.y-1] not in visitedbfs:
        bfs.append(solverNode(current.steps + 1, current, current.x, current.y-1))
    if mapping[current.x][current.y].south == 0 and [current.x, current.y+1] not in visitedbfs:
        bfs.append(solverNode(current.steps + 1, current, current.x, current.y+1))
    if mapping[current.x][current.y].west == 0 and [current.x-1, current.y] not in visitedbfs:
        bfs.append(solverNode(current.steps + 1, current, current.x-1, current.y))
    if mapping[current.x][current.y].east == 0 and [current.x+1, current.y] not in visitedbfs:
        bfs.append(solverNode(current.steps + 1, current, current.x+1, current.y))
        
iterNode = currentSol

while True:
    par = iterNode.parent
    if par == None:
        break
    xdata = [iterNode.x+0.5, par.x + 0.5]
    ydata = [iterNode.y+0.5, par.y + 0.5]
    plt.plot(xdata, ydata, color = 'blue', linewidth=2)
    iterNode = par

plt.plot(0.5, gridSize-1+0.5, marker = "o", markersize = 8)
plt.plot(gridSize-1+0.5, 0.5, marker = "*", markersize = 8)
plt.show()

