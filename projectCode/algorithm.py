import math
from heapq import *

class pathFinder():
    """
    Class for finding nearby connetions for
    a node on the canvas
    """
    def __init__(self, given_width, given_height):
        """
        Function that initializes the class
        """
        self.maxWidth = given_width
        self.maxHeight = given_height
        self.neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        self.rBFS_destination = None
        self.rBFS_gScore = None
        self.rBFS_fScore = None
        self.rBFS_path = None
        self.enable_logging = True
        self.maxQueueSizeAStar = 0
        self.maxQueueSizeRBFS = dict()
        if self.enable_logging:
            self.initMaxQueueSizeRBFS()          #added here to cummulate values from all the call, otherwise has to be added in pathFindRecursiveBestFirstSearch

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

    def heuristic(self, first_location, second_location):
        """
        Function that calculates the Eucledian distance 
        between two points a and b on canvas
        return: the distance between the two points
        """
        return math.sqrt(pow(first_location[0] - second_location[0],2) + 
                         pow(first_location[1] - second_location[1],2))

    def getGraphMapEmpty(self, defaultValue):
        """
        Function returning an empty map of all the points
        on the canvas
        defaultValue: any arithmetic value
        return: map of all points to defaultValue
        """
        map_with_default_values = {}
        for i in range(0,640):
            for j in range(0,480):
                map_with_default_values[(i, j)] = defaultValue
        return map_with_default_values
    
    def initMaxQueueSizeRBFS(self):
        for i in range(0,640):
            for j in range(0,480):
                self.maxQueueSizeRBFS[(i,j)] = 0
                
    def getMaxQueueSizeRBFS(self):
        totalCount = 0
        for city in self.maxQueueSizeRBFS.keys():
            totalCount += self.maxQueueSizeRBFS[city]
        return totalCount

    def pathFindAstar(self, start, goal):
        """
        Algorithm for finding the paht from start to
        goal location using A-star algorithm
        
        TODO:
        1. return the length of path, to reduce computation
        2. change from tuple to list for inputs of start and goal
        """
        openList = []
        openSet = set()
        cameFrom = self.getGraphMapEmpty(None)
        gScore = self.getGraphMapEmpty(float('inf'))
        gScore[start] = 0
        fScore = self.getGraphMapEmpty(float('inf'))
        fScore[start] = self.heuristic(start, goal)
        heappush(openList, (fScore[start], start))
        openSet.add(start)
        if self.enable_logging:
            self.maxQueueSizeAStar += 1
        while openList:
            current = heappop(openList)[1]
            if self.enable_logging:
                self.maxQueueSizeAStar -= 1
            openSet.discard(current)
            if current == goal:
                path = []
                while current in cameFrom:
                    path.append(current)
                    current = cameFrom[current]
                path.append(start)
                path.reverse()
                # print("Total cities expanded in A* algorithm: " + str(self.totalCitiesExpandedAStar()))
                if self.enable_logging:
                    print("cummulative max queue size in A* algorithm: " + str(self.maxQueueSizeAStar))
                return path
            connections = self.getConnections(current)
            for connection in connections:
                # tentative_gScore = gScore[current] + heiuristic(current, connection)
                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[connection]:
                    cameFrom[connection] = current
                    gScore[connection] = tentative_gScore
                    fScore[connection] = gScore[connection] + self.heuristic(connection, goal)
                    if connection not in openSet:
                        heappush(openList, (fScore[connection], connection))
                        openSet.add(connection)
                        if self.enable_logging:
                            self.maxQueueSizeAStar += 1
        return False

    def rBFS_utility(self, current, fLimit, parent):
        if self.enable_logging:
            tempQueueSize = 0
        if current == self.rBFS_destination:
            return current, fLimit
        successors = self.getConnections(current)
        if not successors:
            return None, float('inf')
        successorSet = []
        for successor in successors:
            if self.enable_logging:
                tempQueueSize += 1
            self.rBFS_gScore[successor] = self.rBFS_gScore[current] + 1
            self.rBFS_fScore[successor] = max(self.rBFS_gScore[successor] + self.heuristic(successor, self.rBFS_destination), self.rBFS_fScore[current])
            heappush(successorSet, (self.rBFS_fScore[successor], successor))
        if self.enable_logging:
            if self.maxQueueSizeRBFS[current] != 0:
                if self.maxQueueSizeRBFS[current] < tempQueueSize:
                    self.maxQueueSizeRBFS[current] = tempQueueSize
            else:
                self.maxQueueSizeRBFS[current] = tempQueueSize
        while True:
            best = heappop(successorSet)
            bestFlimit = best[0]
            if bestFlimit > fLimit:
                self.rBFS_path.pop()
                return None, bestFlimit
            if len(successorSet) != 0:
                alternative = heappop(successorSet)
                heappush(successorSet, alternative)
                self.rBFS_path.append(best[1])
                result, bestFlimit = self.rBFS_utility(best[1], min(fLimit, alternative[0]), current)
                heappush(successorSet, (bestFlimit, best[1]))
                if result != None:
                    return result, bestFlimit
            else:
                self.rBFS_path.append(best[1])
                result, bestFlimit = self.rBFS(best[1], fLimit, current)
                heappush(successorSet, (bestFlimit, best[1]))
                if result != None:
                    return result, bestFlimit

    def pathFindRecursiveBestFirstSearch(self, start, goal):
        # self.initMaxQueueSizeRBFS()
        self.rBFS_path = list()
        self.rBFS_destination = goal
        self.rBFS_gScore = self.getGraphMapEmpty(0)
        self.rBFS_fScore = self.getGraphMapEmpty(0)
        self.rBFS_fScore[start] = self.heuristic(start, goal)
        try:
            self.rBFS_utility(start, float('inf'), None)
        except Exception as e:
            if self.enable_logging:
                print("cummulative max queue size in RBFS algorithm: " + str(self.getMaxQueueSizeRBFS()))
            print "maximum recursion depth exceeded"
            return False
        if self.enable_logging:
            print("cummulative max queue size in RBFS algorithm: " + str(self.getMaxQueueSizeRBFS()))        
        return self.rBFS_path
