class heapElement :
    def __init__(self, key, value) :
        self.key = key
        self.value = value

    def printElement(self) :
        print (self.key, self.value)

    # if current element is smaller than that element, return True
    def less(self,that) :
        if self.value <= that.value :
            return True
        else :
            return False   

class heap :
    def __init__(self) :
        self.h = [None]
        self.position = {}
        self.size = 0

    def appendheap(self, key, value) :
        self.h.append(heapElement(key, value))
        self.size +=1
        self.position[key] = self.size

    def checkheap(self) :
        if len(self.h) != self.size + 1 :
            print 'heap size wrong'
            return False
        for key in self.position :
            try :
                if self.h[self.position[key]].key != key :
                    print 'heap position wrong'
                    return False
            except :
                print 'checkheap exception', key
                sys.exit(0)
        for i in range(1, self.size/2+1) :
            if  self.h[i].value > self.h[2*i].value :
                print 'wrong order', i, 2*i
                return False
            if 2*i+1 <= self.size and self.h[i].value > self.h[2*i+1].value :
                print 'wrong order', i, 2*i+1
                return False

        return True

    # swap the i-th and j-th elements
    def swap(self, i, j) :
        # swap the position first
        self.position[self.h[i].key] = j
        self.position[self.h[j].key] = i
        # the switch the element
        tmp_element = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = tmp_element
    # bubble up the i-th element in the heap, return the final position
    def bubbleUp(self, i) :
        while i > 1 and self.h[i].less(self.h[i/2]) :
            self.swap(i, i/2)
            i = i / 2
        return i

    # bubble down then i-th element in the heap, return the final position
    def bubbleDown(self, i) :
        while 2 * i <= self.size :
            j = 2 * i
            # pick the smaller of the two children nodes
            if j < self.size and self.h[j+1].less(self.h[j]) :
                j += 1
            if self.h[i].less(self.h[j]) :
                break
            self.swap(i,j)
            i = j
        return i

    # pop the minimum of the heap
    def popheap(self) :
        return_element = self.h[1]
        self.swap(1,self.size)
        del self.h[self.size]
        del self.position[return_element.key]
        self.size -= 1
        self.bubbleDown(1)
        return return_element

    # check order of the heap
    # insert
    def pushheap(self, element) :
        self.size += 1
        self.h.append(element)
        self.position[element.key] = self.size
        self.bubbleUp(self.size)

    def delKey(self, key) :
        pos = self.position[key]
        if pos == self.size :
            del self.h[self.size]
            self.size -= 1
            del self.position[key]
            return
        # swap the current position with the last element
        self.swap(pos, self.size)
        del self.h[self.size]
        self.size -= 1
        del self.position[key]
        # decide whether need to bubble up or down
        if self.h[pos].less(self.h[pos/2]) :
            self.bubbleUp(pos)
        elif pos * 2 <= self.size :
            j = pos * 2
            if j < self.size and self.h[j+1].less(self.h[j]) :
                j += 1
            if self.h[j].less(self.h[pos]) :
                self.bubbleDown(pos)
  


    def printheap(self) :
        print 'size: ', self.size
        for item in self.h[1:] :
            item.printElement()
        print self.position

