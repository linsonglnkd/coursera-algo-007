from heap import *

left_heap = heap('desc')
right_heap = heap('asc')

a = []
m = []

i = 0
count = 0
for line in open('Median.txt') :
    i += 1
    item = int(line.strip())
    # the first element
    if i == 1 :
        left_heap.pushheap(heapElement(str(i),item))
        m.append(item)
        continue
    # check if the current value is bigger than the largest of the left heap
    # if larger, then push to the left (odd) or right (even) and move the right root to left it needed
    # if not larger, either push the left (odd) or move root of left to right and push to left
    if item > left_heap.h[1].value :
        if i % 2 == 0 :
            right_heap.pushheap(heapElement(str(i),item))
        else :
            # if value > right root, move right root
            if item > right_heap.h[1].value :
                tmp = right_heap.popheap()
                right_heap.pushheap(heapElement(str(i),item))
                left_heap.pushheap(tmp)
            # if left < value < right, insert to left
            else :
                left_heap.pushheap(heapElement(str(i),item))
    else :
        if i % 2 == 0 :
            tmp = left_heap.popheap()
            right_heap.pushheap(tmp)
            left_heap.pushheap(heapElement(str(i),item))
        else :
            left_heap.pushheap(heapElement(str(i),item))

    m.append(left_heap.h[1].value)
print len(m)
'''
sum = 0
for item in m :
    sum += item
print sum % 10000
'''

