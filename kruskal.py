g1 = {
       2 : [['S','A'],['A','B'],['C','B'],['E','T']],
       3 : [['S','C'],['B','D'],['D','E'],['F','E']],
       4 : [['F','T']],
       5 : [['S','B']],
       6 : [['B','F'],['A','D'],['D','T']],
       7 : [['C','F']]
       }

g2 = {
       1 : [['A','B']],
       2 : [['A','C'],['C','F'],['F','H'],['F','J']],
       3 : [['A','D'],['B','C'],['E','F'],['F','G'],['F','I'],['I','K']],
       4 : [['D','F'],['B','E'],['E','H'],['H','K'],['I','J'],['J','K']],
       5 : [['C','D'],['B','F'],['D','G'],['H','I']]
}


def kruskal(graph):
       weight = [i for i in graph.keys()] #like queue
       visited = []
       total_w = 0
       while weight:
              current_weight = weight[0]
              
              for i in graph[current_weight]:
                     
                     append_check = False
                     print('I = ' ,i)
                     for j in range(len(visited)):
                            print('J = ' ,j)
                            # break loop when both are visited
                            if i[0] in visited[j] and i[1] in visited[j]: 
                                   append_check = True
                                   print('i1(0) = ' ,i[0], ',',i[1])
                                   # print('total = ',total_w)
                                   break
                            # append only one node that haven't visited
                            if i[0] in visited[j] and i[1] not in visited[j]:
                                   visited[j].append(i[1])
                                   total_w += current_weight
                                   append_check = True
                                   print('i2(0) = ' ,i[0], ',',i[1])
                                   # print('total = ',total_w)
                                   break
                            elif i[1] in visited[j] and i[0] not in visited[j]:
                                   visited[j].append(i[0])
                                   total_w += current_weight
                                   append_check = True
                                   print('i3(0) = ' ,i[0], ',',i[1])
                                   # print('total = ',total_w)
                                   break
                            
                     # add both nodes that haven't visited yet      
                     if not append_check : 
                            visited.append(i)
                            print('visited = ',visited)
                            total_w += current_weight
                            print('total = ',total_w)
                     
                     # check connection of different node group
                     visited.sort(reverse = True, key = lambda x:len(x)) # main group node (longest) is at visited[0]
                     print('visit = ',visited)
                     for small_group in range(1,len(visited)):
                            print('small = ',small_group)
                            for node in visited[small_group]:
                                   print('node = ',node)
                                   if node in visited[0]:
                                          print('visit(0)',visited[0])
                                          print('node2 = ',node)
                                          visited[small_group].remove(node) #remove replication node
                                          print('small2 = ',small_group)
                                          for i in visited[small_group]:
                                                 print('I1 = ',i)
                                                 print('small3 = ',small_group)
                                                 print('visit(small) = ',visited)
                                                 visited[0].append(i) # append the rest node to the main group
                                                 print('visit(0) = ',visited)
                                          visited.remove(visited[small_group]) # remove smaller group node
                                          break
                            
                     print(visited)
                     print(total_w)
              weight.pop(0)
       return visited, total_w

# # Input part
# edge = int(input("How many edges : "))
# graph = {}

# for i in range(edge):
#        print(graph)
#        node = [ i for i in input("nodes connected : ").split()]
#        weight = int(input("weight : "))

#        if weight not in graph.keys():
#               graph[weight] = [node]
#               continue

#        graph[weight].append(node)


path, weight_sum = kruskal(g1)
print(path)
print(weight_sum)