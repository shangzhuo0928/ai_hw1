import csv
import numpy as np
import copy

edgeFile = 'edges.csv'

data = []

with open(edgeFile, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)  
    next(reader)
    for row in reader:
        s, e, d = int(row[0]), int(row[1]), float(row[2])
        data.append((s,e,d))


def dfs(start, end):
    # Begin your code (Part 2)
    st = []
    num = 0 # count visited nodes
    st.append((start, 0.0, [start])) #(new start node, distance, path list)
    g = [] # store poped node data
    used = [] # if node is used
    while 1:
        g = st.pop() # pop first node
        if g[0] not in used:
            
            if g[0] == end: # if the poped node number is end node, then end loop
                break
            used.append(g[0])
            num += 1 # pop a node +1
            for d in data:
                if d[0] == g[0]:
                    if d[1] not in used:
                        p1 = g[2].copy() # use copy to make data can separate
                        p1.append(d[1])
                        st.append((d[1], round(g[1]+d[2], 3), p1)) #round to .3f
                        del d
        
    return g[2], g[1], num
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
