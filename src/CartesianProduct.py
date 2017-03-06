

class CartesianProduct(object):
	"""docstring for CartesianProduct"""
	def __init__(self, word1, word2):

		cartesianProductMatrix = [[]]

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
		for s in xrange(0, len(shorterWord.listOfPhonemes)):
			
			currentRow = []

			for l in xrange(0, len(longerWord.listOfPhonemes)):
				newOrderedPair = OrderedPair.OrderedPair(shorterWord.listOfPhonemes[s], longerWord.listOfPhonemes[l], l)
				currentRow.append(newOrderedPair)

			cartesianProductMatrix.append(currentRow)

	def resetOrderedPairRVs(self):

		currentRow = None

		for i in xrange(0, len(cartesianProductMatrix)):

			currentRow = cartesianProductMatrix[i]

			for j in xrange(0, len(currentRow)):
				
				currentRow[j].resetRV()

	def removeTopRow(self):
		cartesianProductMatrix.pop(0)



		
		