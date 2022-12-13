
import math

# g1 = { "S" : {"A":2,"B":5,"C":3},
#           "A" : {"S":2,"B":2,"D":6},
#           "B" : {"S":5,"A":2,"C":2,"D":3,"F":6},
#           "C" : {"S":3,"B":2,"F":7},
#           "D" : {"A":6,"B":3,"E":3,"T":6},
#           "E" : {"D":3,"F":3,"T":2},
#           "F" : {"B":6,"C":7,"E":3,"T":4},
#           "T" : {"D":6,"E":2,"F":4}
#         }

g1 = { "a" : {"b":4,"h":8},
        "b" : {"a":4,"c":8,"h":11},
        "c" : {"b":8,"i":2,"f":4,"d":7},
        "d" : {"c":7,"f":14,"e":9},
        "e" : {"d":9,"f":10},
        "f" : {"d":14,"c":4,"g":2,"e":10},
        "g" : {"f":2,"i":6,"h":1},
        "h" : {"a":8,"i":7,"g":1},
        "i" : {"c":2,"h":7,"g":6}
        }

def dijkstra(start,end): # start node, destination node

    node = {i: [math.inf,""] for i in g1} # {node: [weight, from what node]}
    node[start] = [0,""] # assign the start node [weight = 0, from nothing]
    visited = [] # to store visited node
    path = [end] # store path track from end to start
    queue = [start] # store node to visit next

    while queue: # run while there's still node to visit

        # loop through child node of first queue 
        for i in g1[queue[0]]: 

            # if child not visited & (weight from parent to child + weight of parent < child weight)
            if i not in visited and g1[queue[0]][i] + node[queue[0]][0] < node[i][0]: 
                node[i][0] = g1[queue[0]][i] + node[queue[0]][0] # child weight = weight from parent to child + weight of parent
                node[i][1] = queue[0] # updated where weight from (parent node)
                queue.append(i) # append child in queue to visit next

        visited.append(queue[0]) # append parent to visited 
        queue.pop(0) # remove parent from queue

    #path

    track = end # assign current node to track back from end to start

    #run while start not in path (not reached start) 
    while start not in path:
        path.append(node[track][1]) # append where track node from to path
        track = node[track][1] # assign new track value to where track node from

    return node[end][0], path[::-1] # return destination minimun weight & path
    

# Input part

num_nodes = int(input("How many nodes : "))
graph = {}
for i in range(num_nodes):
    node = input("Node : ")
    connect = {i[0]:int(i[1:]) for i in input("Connect : ").split()}
    
    graph[node] = connect

start = input("Start node : ")
end = input("Destination node : ")

distance, path = dijkstra(start,end)
print("Distance :",distance)
print("Path :",end="")
for i in path:
    print(i,end=" ")
print()