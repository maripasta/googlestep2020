from collections import defaultdict
import random

class Graph:
    def __init__(self, startid, endid, graph):
        self.node = startid
        self.endnode = endid
        self.neighbors = graph
    
    #normal dfs
    def dfs(self):
        visited = []
        def dfs_recursive(node):
            if node not in visited:
                visited.append(node)
                if node == self.endnode:
                    return visited
                for neighbor in self.neighbors[node]:
                    path = dfs_recursive(neighbor)
                    if path is not None: 
                        return path
        return dfs_recursive(self.node)

    #random dfs, shuffles the neighbors order
    def random_dfs(self):
        visited = []
        def dfs_recursive(node):
            if node not in visited:
                visited.append(node)
                if node == self.endnode:
                    return visited
                random.shuffle(self.neighbors[node])
                for neighbor in self.neighbors[node]:
                    path = dfs_recursive(neighbor)
                    if path is not None: 
                        return path
        return dfs_recursive(self.node)

#start from ID #1 (adrian) and end at ID #15 (cynthia)
#get the ID of adrian and cynthia from file
namedict = {}
with open('nicknames.txt') as nicknamesfile:
    for line in nicknamesfile:
        ID, nickname = line.strip().split()
        namedict[nickname] = int(ID)
endid = namedict['cynthia']
startid = namedict['adrian']
graph = defaultdict(list)

#create graph dict from file
with open('links.txt') as linksfile:
    for line in linksfile:
        ID, follow = map(int, line.strip().split())
        graph[ID].append(follow)

g = Graph(startid, endid, graph)

#does random dfs and prints the shortest route out of the trials
prevpath = list(g.random_dfs())
for i in range(15):
    currentpath = list(g.random_dfs()) 
    if len(currentpath) < len(prevpath):
        prevpath = currentpath
print(prevpath)
