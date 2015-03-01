from heap import *
import sys

G = []
V = []
E = []

def readGraph() :
    V = []
    E = []
    for line in open('/Song/Coursera/coursera-algo-007/week_5/dijkstraData.txt') :
        items = line.split()
        V.append(int(items[0]))
        edge_for_one_node = [[int(x.split(',')[0]), float(x.split(',')[1])] for x in items[1:]]
        E.append(edge_for_one_node)
    return [V,E]

G = readGraph()

#V = [1,2,3,4]
#E = [[[2,1],[3,6],[4,10]],[[3,2],[4,3]],[[4,3]],[]]
#G = [V,E]

# get the distance from node u to node v in graph G
def dist(Graph, u, v) :
    if u == v :
        return 0.0
    else :
        for [node_i, dist_i] in Graph[1][u-1] :
            if node_i == v :
                return dist_i

def shortDist(Graph, start_node) :
    # both dijkstra_dist_1 and dijkstra_dist_2 are dict
    # 'node':short_distance
    # dijkstra_dist_1 is the one with finished nodes
    # dijkstra_dist_2 is the one with nodes to be calculated
    dijkstra_dist_1 = {str(start_node):0}
    dijkstra_dist_2 = {str(node):1000000.0 for node in Graph[0] if node != start_node}
    current_node = start_node
    current_dist = 0.0
    count = 0
    my_heap = heap()
    for node in dijkstra_dist_2 :
        my_heap.pushheap(heapElement(node,dijkstra_dist_2[node]))

    while True :
        if len(G[1][current_node-1]) == 0 :
            break
        if len(dijkstra_dist_2) == 0 :
            break
        for [node_i, dist_i] in G[1][current_node-1] :
            if str(node_i) in dijkstra_dist_2 :
                if current_dist + dist_i < dijkstra_dist_2[str(node_i)] :
                    try :
                        if current_node == 144 and node_i == 68 :
                            print 'before delete'
                            print my_heap.checkheap()
                            print my_heap.size
                            print my_heap.position['68']
                            #print my_heap.h[1].key, my_heap.h[1].value
                        my_heap.delKey(str(node_i))
                        if current_node == 144 and node_i == 68 :
                            print 'after delete', my_heap.checkheap()
                        my_heap.pushheap(heapElement(str(node_i),current_dist + dist_i))
                        dijkstra_dist_2[str(node_i)] = current_dist + dist_i
                    except :
                        print 'error', current_node, node_i, current_dist + dist_i
                        #my_heap.printheap()
                        sys.exit(1)
        current_element = my_heap.popheap()
        current_node = int(current_element.key)
        current_dist = current_element.value

        del dijkstra_dist_2[str(current_node)]

        if current_dist > 1000000 - 1 :
            break
        dijkstra_dist_1[str(current_node)] = current_dist
        print 'count: ', count, (current_node, current_dist)

        count += 1
        if count > 10000 :
            break
    return dijkstra_dist_1

dist = shortDist(G,1)

print dist['7']
print dist['37']
print dist['59']
print dist['82']
print dist['99']
print dist['115']
print dist['133']
print dist['165']
print dist['188']
print dist['197']
#2599,2610,2947,2052,2367,2399,2029,2442,2505,3068