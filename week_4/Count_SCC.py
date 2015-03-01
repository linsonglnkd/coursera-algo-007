import pickle

leader_array = pickle.load( open( "/Song/Coursera/coursera-algo-007/week_4/leader.pickle", "rb" ) )
cluster_size = {}

for node in leader_array :
    if str(node) in cluster_size :
        cluster_size[str(node)] += 1
    else :
        cluster_size[str(node)] = 1

print cluster_size['1']
