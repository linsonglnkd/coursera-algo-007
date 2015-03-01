import copy
import sys
import pickle
#V = [1,2,3,4,5,6,7,8,9]
#E = [[7],[5],[9],[1],[8],[3,8],[9,4],[2],[6]]
#G = [V,E]

#sys.setrecursionlimit(10000)

# read in the graph

V = range(1, 875715)
E = [[]] * len(V)
for line in open('/Song/Coursera/coursera-algo-007/week_4/SCC.txt') :
	items = line.strip().split()
	if len(E[int(items[0])-1]) == 0 :
		E[int(items[0])-1] = [int(items[1])]
	else :
		E[int(items[0])-1].append(int(items[1]))

#sys.exit(0)
#V = [1,2,3,4,5,6,7,8,9]
#E = [[4],[8],[6],[7],[2],[9],[1],[5,6],[3,7]]

G = [V,E]
visited = [0] * len(V)
finish_time = []
leader = [0] * len(V)

# reverse all arcs in a graph
def reverse(G) :
	V_rev = copy.deepcopy(G[0])
	E = G[1]
	E_rev = [[]] * len(V)
	for i in range(len(V)) :
		start_node = i + 1
		for end_node in E[i] :
			#print 'start_node, end_node', start_node, end_node
			if len(E_rev[end_node-1]) == 0 :
				E_rev[end_node-1] = [start_node]
			else :
				E_rev[end_node-1].append(start_node)
			#print 'Erev',E_rev
	G_rev=[V_rev, E_rev]
	return G_rev
		

def DFS(Graph, order_list) :
	V = copy.deepcopy(Graph[0])
	E = copy.deepcopy(Graph[1])
	stack = []
	count = 0
	for node in order_list :
		if visited[node-1] == 0 and len(stack) == 0 :
			visited[node-1] = 1
			leader[node-1] = node
			stack.append(node)
			# push into stack part
			pos = len(stack) - 1
			while len(stack) > 0 :
				if len(E[stack[-1]-1]) == 0 :
					finish_time.append(stack.pop())
					a = len(finish_time)
					if a % 100 == 0 :
						print a
					continue
				#print 'stack, edge:', stack, E[stack[-1]-1]
				end_node = E[stack[-1]-1].pop()

				if visited[end_node-1] == 0 :
					stack.append(end_node)
					visited[end_node-1] = 1
					leader[end_node-1] = node
					continue


pickle.dump(G, open( "/Song/Coursera/coursera-algo-007/week_4/G.pickle", "wb" ))

G_rev = reverse(G)
pickle.dump(G_rev, open( "/Song/Coursera/coursera-algo-007/week_4/G_rev.pickle", "wb" ))

order_list = copy.deepcopy(V)
DFS(G_rev, order_list)
print 'done G_rev'
pickle.dump(finish_time, open( "/Song/Coursera/coursera-algo-007/week_4/finish_time.pickle", "wb" ))

finish_time.reverse()

visited = [0] * len(V)
leader = [0] * len(V)

DFS(G, finish_time)


pickle.dump(leader, open( "/Song/Coursera/coursera-algo-007/week_4/leader.pickle", "wb" ))

'''
a = pickle.load( open( "/Song/Coursera/coursera-algo-007/week_4/leader.pickle", "rb" ) )
print a
'''