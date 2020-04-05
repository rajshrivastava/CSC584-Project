import math
from heapq import *

class pathFinder():
    """
    Class for finding nearby connetions for
    a node on the canvas
    """
    def __init__(self, x, y):
        """
        Function that initializes the class
        """
        self.maxWidth = x
        self.maxHeight = y
        self.neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    
    def checkValid(self, fromNode, new_x, new_y):
        """
        Checks if the location is accessible or not
        return: bool value
        """
        if new_x < 0 or new_x > self.maxWidth:
            return False
        elif new_y < 0 or new_y > self.maxHeight:
            return False
        # elif get(new_x, new_y) != -1:
        #     return False
        else:
            return True
    
    def getConnections(self, fromNode):
        """
        Function returns a list of nearby accessible
        nodes from the give fromNode
        fromNode: node whose connections has to be returned
        return: list of connections
        """
        fromNodeNeighbors = []
        for i in range(0,8):
            new_x = self.neighbors[i][0] + fromNode[0]
            new_y = self.neighbors[i][1] + fromNode[1]
            if self.checkValid(fromNode, new_x, new_y):
                location = (new_x, new_y)
                fromNodeNeighbors.append(location)
        # if len(fromNodeNeighbors) == 0:
        #     print("no neighbors to return")
        return fromNodeNeighbors

def heiuristic(a,b):
    """
    Function that calculates the Eucledian distance 
    between two points a and b on canvas
    return: the distance between the two points
    """
    return math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))

def getGraphMapEmpty(defaultValue):
    """
    Function returning an empty map of all the points
    on the canvas
    defaultValue: any arithmetic value
    return: map of all points to defaultValue
    """
    a = {}
    for i in range(0,640):
        for j in range(0,480):
            a[(i, j)] = defaultValue
    return a

def pathFindDijkstra(pathFinderObject, start, goal):
    """
    Algorithm for finding the paht from start to 
    goal location using A-star algorithm
    
    TODO: return the length of path, to reduce computation
    """
    openList = []
    openSet = set()
    cameFrom = getGraphMapEmpty(None)
    gScore = getGraphMapEmpty(float('inf'))
    gScore[start] = 0
    fScore = getGraphMapEmpty(float('inf'))
    fScore[start] = heiuristic(start, goal)
    heappush(openList, (fScore[start], start))
    openSet.add(start)
    while openList:
        current = heappop(openList)[1]
        openSet.discard(current)
        if current == goal:
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path.append(start)
            path.reverse()
            return path
        connections = pathFinderObject.getConnections(current)
        for connection in connections:
            # tentative_gScore = gScore[current] + heiuristic(current, connection)
            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore[connection]:
                cameFrom[connection] = current
                gScore[connection] = tentative_gScore
                fScore[connection] = gScore[connection] + heiuristic(connection, goal)
                if connection not in openSet:
                    heappush(openList, (fScore[connection], connection))
                    openSet.add(connection)
    return False
