# heap
#[0,1,2,3,
#[3, 5 , 7, 12, 11, 9, 8]
from unittest.mock import right


class Node:
    def __init__ (self, x):
        self.value = x
        self.parent = 0
        self.left = 0
        self.right = 0
class Tree:
    def __init__(self):
        self.root = 0
        self.size = 0


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def left(self, i):
        if (2*i+1) < self.size:
            return self.arr[2*i+1]
        else:
            return None
    def right(self, i):
        if (2*i+2) < self.size:
            return self.arr[2*i+2]
        else:
            return None
    def parent(self,i):
        if ((i-1)//2) < self.size:
            return self.arr[(i-1)//2]
        else:
            return None
    def SiftDown(self, value, i):
        right = self.right(i)
        left = self.left(i)
        if not left and not right:
            return
        if value > right and value > left:
            return
        else:
            if right > left:
                self.arr[i] = right
                self.arr[2*i+2] = value
                self.SiftDown(value, 2*i+2)
            else:
                self.arr[i] = left
                self.arr[2*i+1] = value
                self.SiftDown(value, 2*i+1)
    def SiftUp(self, value, i):
        parent = self.parent(i)
        if not parent:
            return
        if value > parent:
            self.arr[(i - 1) // 2] = value
            self.arr[i] = parent
            self.SiftUp(value, (i - 1) // 2)
        else:
            return
    def append(self):
        self.arr.append(value)
        self.size+=1
        self.SiftUp(value,self.size-1)
    def getmax(self):
        return self.arr[0]

    def pop(self):
        self.arr[0],self.arr[-1]=self.arr[-1],self[0]
        self.size-=1
        self.arr.pop()
        self.SiftDown(self.arr[0],0)
    def heapify(self):
        pass

h = Heap([15,5,7,4,2,6,3])
h.SiftDown(1,0)
h.SiftUp(10, 3)
print(h.arr)
h.pop()
print(h.arr)
h.append(10)
print(h.arr)