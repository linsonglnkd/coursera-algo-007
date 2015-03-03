from heap import *

heap1 = heap('asc')
print heap1.size
heap1.pushheap(heapElement('a',2))
heap1.pushheap(heapElement('b',7))
heap1.pushheap(heapElement('c',5))
heap1.pushheap(heapElement('d',4))
heap1.pushheap(heapElement('e',6))
heap1.pushheap(heapElement('f',8))

a = heap1.size
heap1.h[1].value = 1
print heap1.checkheap()
for i in range(a) :
    heap1.popheap().printElement()