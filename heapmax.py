# coding: utf-8

def heapMax(targetList):
	"""
	heapMax
	指定のheapSizeのmax heap propertyの配列を作成
	:param targetList: heap propertyにするlist
	:return heap: list
	"""

	HEAP_SIZE = len(targetList)

	heap = list(targetList)
	# create a heap list
	for i in range(0, HEAP_SIZE):
		val = heap[i]
		insert(val, heap, i)
	return heap


def insert(val, heap, counter):
	"""
	insert
	heap listにvalをmax heap propertyになるよう代入
	最初にHEAP_SIZE + 1の全ての値が0のheap listを用意しておくこと。
	:param val: list
	:param heap: list
	:param counter: int
	"""
	i = counter
	while ((i != 0) and (heap[(i-1)//2] < val)):
		heap[i] = heap[(i-1)//2]
		i = (i-1)//2
	heap[i] = val
