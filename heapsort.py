from math import ceil
from random import randint

# left   => n * 2 + 1
# right  => n * 2 + 2
# father => int(ceil(n / 2))


class MaxHeap:

    def __init__(self, items):
        self.heap = items
        self.heapify()

    def push(self, data):
        self.heap.append(data)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 1:
            self.switch(0, len(self.heap) - 1)
            largest = self.heap.pop()
            self.sift_down(0)
        elif len(self.heap) == 1:
            largest = self.heap[0]
        else:
            largest = False
        return largest

    def switch(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, pos):
        if pos == 0:
            return
        # father is greater than current value
        father = int(ceil(pos / 2)) - 1
        if self.heap[pos] > self.heap[father]:
            self.switch(pos, father)
            self.sift_up(father)

    def sift_down(self, pos, end=0):
        if not end:
            end = len(self.heap)

        left = pos * 2 + 1
        right = pos * 2 + 2
        largest = pos

        if end > left and self.heap[left] > self.heap[largest]:
            largest = left

        if end > right and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != pos:
            self.switch(pos, largest)
            self.sift_down(largest, end)

    def heapify(self):
        end = int(ceil(len(self.heap) / 2))
        for i in range(end, -1, -1):
            self.sift_down(i)

    def sort(self):
        size = len(self.heap)
        while size > 1:
            self.switch(0, size - 1)
            self.sift_down(0, size - 1)
            size -= 1

# - - - - - - - - - TESTING - - - - - - - - - #


my_arr = [4, 23, 53, 20, 11, 8, 2, 100, 15, 44, 0, 27]
my_random_arr = [randint(0, 100) for _ in range(20)]

print('Initial array:')
print(my_random_arr, end='\n\n')

print('Converted to heap')
my_heap = MaxHeap(my_random_arr)
print(my_heap.heap, end='\n\n')

print('Taking the first value of the heap: {0}'.format(my_heap.pop()))
print(my_heap.heap, end='\n\n')

print('Sorting array:')
my_heap.sort()
print(my_heap.heap)
