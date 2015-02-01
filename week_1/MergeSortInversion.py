# Calculate number of inversions using merge sort

import numpy as np
import copy
import timeit

def MergeSortInv(a,i,j) :
    if i == j :
        return 0
    x = MergeSortInv(a, i, (i+j)/2)
    y = MergeSortInv(a, (i+j)/2+1, j)
    # merge piece
    z = 0
    b = copy.copy(a[i:j+1])
    pointer_1 = i
    pointer_2 = (i+j)/2 + 1
    for k in range(i,j+1) :
        if pointer_1 > (i+j)/2 :
            b[k-i] = a[pointer_2]
            pointer_2 += 1
            continue
        if pointer_2 > j :
            b[k-i] = a[pointer_1]
            pointer_1 += 1
            continue
        if a[pointer_1] <= a[pointer_2] :
            b[k-i] = a[pointer_1]
            pointer_1 += 1
            continue
        else :
            b[k-i] = a[pointer_2]
            pointer_2 += 1
            z += (i+j)/2 - pointer_1 + 1
    a[i:j+1] = b
    return x + y + z

def BruteForceInv(a) :
    count = 0
    for i in range(0,len(a)-1) :
        for j in range(i+1,len(a)) :
            if a[i] > a[j] :
                count +=1
    return count

a = []
for line in open('IntegerArray.txt') :
    a.append(int(line)) 
'''
print BruteForceInv(a)
2407905288
[Finished in 669.0s]
'''
print MergeSortInv(a,0,99999)
'''
2407905288
[Finished in 1.5s]
'''