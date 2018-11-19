import sys

def findMiddleElement(aList):
	middle = float(len(aList))/2
	if middle % 2 != 0:
		return int(middle - .5)
	else:
		return int(middle)

def doQuickSort(aList):
	if aList:
		middleElement = findMiddleElement(aList)
		left = [x for x in aList if x < aList[middleElement]]
		right = [x for x in aList if x > aList[middleElement]]
		if len(left) > 1:
			left = doQuickSort(left)
		if len(right) > 1:
			right = doQuickSort(right)
		return left + [aList[middleElement]] * aList.count(aList[middleElement]) + right
	return []

if __name__ == "__main__":
	aInput = sys.argv[1]
	inputList = map(int, aInput.strip('[]').split(','))
	print("Incoming List - " + str(inputList))
	sortedList = doQuickSort(inputList)
	print("Sorted List - " +  str(sortedList))