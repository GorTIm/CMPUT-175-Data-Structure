class FixedSizeHeap:
    def __init__(self,Maxsize):
        self.heap = [0]
        self.currentSize = 0
        self.maxsize=Maxsize


    def percUp(self,i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def insert(self,k):
        if self.currentSize<self.maxsize:
            self.heap.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)
        else:
            i=1
            while i*2<self.currentSize:
                if i * 2 + 1 > self.currentSize:
                    i= i * 2                    
                if self.heap[i*2] < self.heap[i*2+1]:
                    i= i * 2+1
                else:
                    i= i * 2
                Max=i
            self.heap[Max]=k                
            self.percUp(self.currentSize)
                        
            

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heap.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

heap = FixedSizeHeap(5)
heap.insert(6)
heap.insert(4)
heap.insert(8)
heap.insert(2)
heap.insert(7)
print(heap.heap)
heap.insert(5)
print(heap.heap)
heap.del_min()
print(heap.heap)
heap.insert(9)
print(heap.heap)
heap.insert(8)
print(heap.heap)