import QuickSort
import QuickSortFirstElement
import BubbleSort
import sys
import time
import random

def main():
	firstSample = random.sample(range(100), 100)
	secondSample = random.sample(range(1500), 1500)
	thirdSample = random.sample(range(3000), 3000)
	forthSample = random.sample(range(4500), 4500)
	fifthSample = random.sample(range(7000), 7000)
	sixthSample = random.sample(range(10000), 10000)

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(firstSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(firstSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(firstSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Primeira Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n----------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(secondSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(secondSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(secondSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Segunda Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n---------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(thirdSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(thirdSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(thirdSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Terceira Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n----------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(forthSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(forthSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(forthSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Quarta Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n--------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(fifthSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(fifthSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(fifthSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Quinta Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n--------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

	startFirstQuickSortTime = time.time()
	QuickSort.doQuickSort(sixthSample)
	totalFirstQuickSortTime = time.time() - startFirstQuickSortTime

	startSecondQuickSortTime = time.time()
	QuickSortFirstElement.doQuickSort(sixthSample)
	totalSecondQuickSortTime = time.time() - startSecondQuickSortTime

	startBubbleSortTime = time.time()
	BubbleSort.doBubbleSort(sixthSample)
	totalBubbleSortTime = time.time() - startBubbleSortTime

	print("----------------- Sexta Amostra -----------------\nQuick Sort (Pivo no centro): %s segundos\nQuick Sort (Primeiro elemento pivo): %s segundos\nBubble Sort: %s segundos\n-------------------------------------------------" % (totalFirstQuickSortTime, totalSecondQuickSortTime, totalBubbleSortTime))

if __name__ == "__main__":
	main()
