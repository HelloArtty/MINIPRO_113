g1 = {
    'A' : ['B','C','F'],
    'B' : ['A','D','J'],
    'C' : ['A','F'],
    'D' : ['B','E','G','H'],
    'E' : ['D','G'],
    'F' : ['H','K'],
    'G' : ['D','E','I','J'],
    'H' : ['D','F','I'],
    'I' : ['G','H','J'],
    'J' : ['B','I','K'],
    'K' : ['F','J']
    }

g2 = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'D'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

def BFS(start_node,graph):
    queue = [start_node]
    # print(queue)
    visited = {start_node : 0} # { node : lvl }
    print('v = ',visited)
    
    while queue:
        now = queue[0]
        print('q = ',queue[0])
        for i in graph[now]:
            print('g = ',graph[now])
            print('i = ',i)
            if i not in visited.keys():
                print('i2 = ',i)
                print('v2 = ',visited )
                visited[i] = visited[now]+1
                print(visited)
                queue.append(i)
                print("q2 = ",queue.append(i))
        queue.pop(0)
        print("q.pop = ",queue)
        
    return visited


# # Input part
# num_nodes = int(input("Total nodes : "))
# graph = {}
    
# for i in range(num_nodes):
#     node = input("node : ")
#     connect = [i for i in input("connect to : ").split()]
#     graph[node] = connect   
#     #print(graph)

# start = input("Start from node : ")

# Output part
bfs = BFS('A',g2)
# bfs = BFS(start,graph)
max_lvl = max(bfs.values())

for lvl in range(max_lvl+1):
    level_node = []
    
    for i in bfs:
        if bfs[i] == lvl:
            level_node.append(i)
    
    print(f"Node level {lvl} = {level_node}")