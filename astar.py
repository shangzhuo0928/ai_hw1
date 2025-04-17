import csv
import numpy as np
from collections import defaultdict #default key aset 
import copy
import heapq

edgeFile = 'edges.csv'
heuristicFile = 'heuristic_values.csv'

data = []

class m:
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(float))
    def set(self, s, e, v):
        self.data[s][e] = v
    def get(self, s, e):
        return self.data[s][e]

hedata = m()

with open(edgeFile, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)  
    next(reader)
    for row in reader:
        s, e, d = float(row[0]), float(row[1]), float(row[2])
        data.append((s,e,d))

with open(heuristicFile, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)  
    first_row = next(reader)
    end = []
    for i in range(1,len(first_row)):  
        end.append(int(first_row[i]))
    for row in reader:
        s = int(row[0])
        for i in range(1,len(row)):  
            hedata.set(str(s), str(end[i-1]), float(row[i]))

def astar(start, end):
    # Begin your code (Part 4)
    all_nodes = set()
    dist = {node: float('inf') for node in all_nodes}
    dist[str(start)] = 0
    q = []
    num = 0 # count visited nodes
    heapq.heappush(q, (hedata.get(str(start), str(end)), 0.0, start, [start])) #use priorty queue (distance, new start node, path list)
    g = [] # store poped node data
    used = [] # if node is used
    while 1:
        g = heapq.heappop(q)
        if g[2] not in used:
            if g[2] == end: # if the poped node number is end node, then end loop
                break
            used.append(g[2])
            num += 1 # pop a node +1
            for d in data:
                if d[0] == g[2]:
                    if d[1] not in used:
                        newc = round(g[1]+d[2], 3)
                        p1 = g[3].copy() # use copy to make data can separate
                        p1.append(d[1])
                        h = round(newc+hedata.get(str(d[1]), str(end)),3)
                        heapq.heappush(q, (h, newc, d[1], p1)) #key to sort is dist for start to n + heuristic of node n, dist round to .3f
                        del d
        
    return g[3], g[1], num
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(426882161, 1737223506)#2270143902, 1079387396) 
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
