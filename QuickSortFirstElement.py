import sys

def doQuickSort(aList):
	if aList:
		left = [x for x in aList if x < aList[0]]
		right = [x for x in aList if x > aList[0]]
		if len(left) > 1:
			left = doQuickSort(left)
		if len(right) > 1:
			right = doQuickSort(right)
		return left + [aList[0]] * aList.count(aList[0]) + right
	return []

if __name__ == "__main__":
	aInput = sys.argv[1]
	inputList = map(int, aInput.strip('[]').split(','))
	print("Incoming List - " + str(inputList))
	sortedList = doQuickSort(inputList)
	print("Sorted List - " +  str(sortedList))