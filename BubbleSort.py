import sys

def doBubbleSort(aList):
	if aList:
		for j in range(0, len(aList)):
			for i in range(0, len(aList) - 1):
				if aList[i] > aList[i + 1]:
					aux = aList[i + 1]
					aList[i + 1] = aList[i]
					aList[i] = aux
		return aList
	return []

if __name__ == "__main__":
	aInput = sys.argv[1]
	inputList = map(int, aInput.strip('[]').split(','))
	print("Incoming List - " + str(inputList))
	sortedList = doBubbleSort(inputList)
	print("Sorted List - " +  str(sortedList))
