import OrderedPair

class CartesianProduct(object):
	"""use itertools.product instead: https://docs.python.org/3/library/itertools.html#itertools.product"""
	def __init__(self, word1, word2):

		self.cartesianProductMatrix = []

		shorterWord = None
		longerWord = None

		'these conditionals find which word is longer and which is shorter'
		if len(word1.listOfPhonemes) < len(word2.listOfPhonemes):
			shorterWord = word1
			longerWord = word2
		else:
			shorterWord = word2
			longerWord = word1

		'creates Cartesian product (shorterWord X longerWord)'
		for s in range(0, len(shorterWord.listOfPhonemes)):
			currentRow = []
			for l in range(0, len(longerWord.listOfPhonemes)):
				newOrderedPair = OrderedPair.OrderedPair(shorterWord.listOfPhonemes[s], longerWord.listOfPhonemes[l], l)
				currentRow.append(newOrderedPair)

			self.cartesianProductMatrix.append(currentRow)

	def resetOrderedPairRVs(self):

		currentRow = None

		for i in range(0, len(self.cartesianProductMatrix)):

			currentRow = self.cartesianProductMatrix[i]

			for j in range(0, len(currentRow)):

				currentRow[j].resetRV()

	def removeTopRow(self):
		self.cartesianProductMatrix.pop(0)
