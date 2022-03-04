#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'detect_deadlock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY agv as parameter.
#

def detect_deadlock(agv):
    if [0] not in agv:
        return 1
#     # Write your code here
#     if [0] in agv:
    g = Graph(len(agv))
    agv_d = {}
    for i in range(1, len(agv)+1):
        agvs = agv[i-1]
        for one in agvs:
            g.addEdge(i, one)
            
    return g.isCyclic()
    

from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v) # add into list of the dict
 
    def isCyclicUtil(self, v, visited, recurStack):

        visited[v] = True
        recurStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recurStack) == True:
                    return True
            elif recurStack[neighbour] == True:
                return True
        recurStack[v] = False
        return False
 
    def isCyclic(self):
        visited = [False] * (self.V+1)
        recurStack = [False] * (self.V+1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recurStack) == True:
                    return 1
        return 0
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    agv_rows = int(input().strip())
    agv_columns = int(input().strip())

    agv = []

    for _ in range(agv_rows):
        agv.append(list(map(int, input().rstrip().split())))

    solution = detect_deadlock(agv)

    fptr.write(str(solution) + '\n')

    fptr.close()