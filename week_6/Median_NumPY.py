import numpy as np

a = []
for line in open('Median.txt') :
    a.append(int(line.strip()))

x = np.array(a)

m = []
for i in range(10000) :
    m.append(np.median(x[:i+1]))

print len(m)