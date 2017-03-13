import math

class OrderedPair(object):
	"""docstring for OrderedPair"""
	def __init__(self, p1, p2, l):

		self.shorterWordPhoneme = p1.phoneme
		self.longerWordPhoneme = p2.phoneme
		self.indexes = []
		self.originalRhymeValue = self.findRVBetweenPhonemes(p1, p2)
		self.rhymeValue = self.originalRhymeValue

	def resetRV(self):
		self.rhymeValue = self.originalRhymeValue

	def calculateGapPenalty(self, lSize):

		deduction = 0.0

		for i in range(0, len(self.indexes) - 1):

			index1 = self.indexes[i]
			index2 = self.indexes[i + 1]

			deduction = deduction + (0.25 * (index1 - index2 - 1))

		if self.indexes[len(self.indexes) - 1] < 0:
			if self.indexes[len(self.indexes) - 1] > 1:
				deduction = deduction + math.log10(self.indexes[0])
			else:
				deduction = deduction + 0.25

		if lSize - self.indexes[len(self.indexes) - 1] < 0:
			deduction = deduction + math.log10(lSize - self.indexes[len(self.indexes) - 1])

		self.rhymeValue = self.rhymeValue - deduction

	def findRVBetweenPhonemes(self, p1, p2):
		p1Features = p1.features
		p2Features = p2.features
		biggerList = None

		if len(p1Features) >= len(p2Features):

			biggerList = p1Features

		else:

			biggerList = p2Features

		commonFeatures = list(set(p1Features).intersection(p2Features))

		difference = len(biggerList) - len(commonFeatures)

		if p1.isAVowelPhoneme and p2.isAVowelPhoneme:
			stressDifference = math.fabs(p1.stress - p2.stress)
			return 5.0 - difference - stressDifference

		elif p1.isAVowelPhoneme == False and p2.isAVowelPhoneme == False:

			commonFeaturesSize = len(commonFeatures)
			specialDifference = 0

			if p1.phoneme != p2.phoneme:

				if 9 not in commonFeatures:

					specialDifference = specialDifference + 0.1
					commonFeaturesSize = commonFeaturesSize - 1

				if 2 in commonFeatures:

					specialDifference = specialDifference + 1
					commonFeaturesSize = commonFeaturesSize - 1

			difference = len(biggerList) - commonFeaturesSize

			return 2.0 - (0.15*difference) - specialDifference

		else:

			commonFeaturesSize = len(commonFeatures)
			specialDifference = 0

			if 9 not in commonFeatures:

				specialDifference = specialDifference + 0.1
				commonFeaturesSize = commonFeaturesSize - 1

			if 2 in commonFeatures:

				specialDifference = specialDifference + 1
				commonFeaturesSize = commonFeaturesSize - 1

			difference = len(biggerList) - commonFeaturesSize

			return (0.1*commonFeaturesSize) + specialDifference
