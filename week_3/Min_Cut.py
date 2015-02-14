import random, time
import copy
import sys
# read in the graph
vertice_orig = []
edge_orig = []
edge_orig_dict = {}

for line in open('/Song/Coursera/coursera-algo-007/week_3/kargerMinCut.txt') :
    count = 0
    for item in line.split() :
        if count == 0 :
            v = item
            vertice_orig.append(int(v))
        else :
            if int(v) < int(item) :
                edge_orig.append([int(v),int(item)])
        count +=1

'''
a = [1,2,3,4,1,2,1]
to_delete = []
for index in range(len(a)) :
    if a[index] == 1 :
        to_delete.append(index)
print to_delete
to_delete.reverse()
print to_delete
for item in to_delete :
    del a[item]
print a

while len(a) > 2 :
    print a.pop()
print a
'''

print vertice_orig

#vertice_orig = [1,2,3,4,5]
#edge_orig = [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]

result = []

for i in range(10000) :
    random.seed(time.clock())
    vertices = copy.deepcopy(vertice_orig)
    edge = copy.deepcopy(edge_orig)

    while len(vertices) > 2 :
        my_rand = random.randrange(len(edge))
        v_from = edge[my_rand][0]
        v_to = edge[my_rand][1]
        # to_delete remembers the position of those self loop edges
        to_delete = []
        for index in range(len(edge)) :
            # update the first node with the second
            if edge[index][0] == v_from :
                edge[index][0] = v_to
            if edge[index][1] == v_from :
                edge[index][1] = v_to
            # always keep the first node in the edge smaller than the second node of the edge
            if edge[index][0] > edge[index][1] :
                swap = edge[index][0]
                edge[index][0] = edge[index][1]
                edge[index][1] = swap
    
            if edge[index][0] == edge[index][1] :
                to_delete.append(index)
        to_delete.reverse()
        for index in to_delete :
            del edge[index]
        vertices.remove(v_from)

    if i % 20 == 0:
        print i

    result.append(len(edge))

result.sort()
print result[:10]

# answer is 17
# 10000 iterations finished in 2562.8 seconds
