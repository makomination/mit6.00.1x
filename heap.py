# coding: utf-8
from random import randrange

HEAP_NUM = 9
heap = [0] * (HEAP_NUM + 1)

def insert(val, heap, counter):
    """
    1. 
    """
    i=counter
    while ((i != 1) and (heap[i//2] < val)):
        heap[i] = heap[i//2]
        i = i//2
    heap[i] = val

for i in range (1, (HEAP_NUM + 1)):
    val = randrange(100)
    insert(val, heap, i)
    print("insert[[{0:d}]: {1:d}".format(i, val))
    
