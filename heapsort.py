# coding: utf-8
def heapSort(aList):
	from heapmax import heapMax
	sortedArr = list()
	list_size = len(aList)
	tList = list(aList)
	tList = heapMax(tList)
	for i in range(list_size-1 , -1, -1):
		if tList[0] >= tList[i]:
			sortedArr.insert(0,tList[0])
			tList[0] = tList[i]
			tList = tList[0:i]
			tList = heapMax(tList)
	return sortedArr
