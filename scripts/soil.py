class Soil(object):
	'''This is my soil class used to monitor important properties related to the soil health.
	'''
	def __init__(self, basicType, P, K):
		self.basicType = basicType
		self.P = P
		self.K = K

	def getPvalue(self):
		return self.P

	def getKvalue(self):
		return self.K

	def fertilize(self, Pfert, Kfert, amount):
		'''Increase the predicted amount of P and K in the soil based on the fertilizer applied.
		PFERT: float, percentage of P in fertilizer
		KFERT: float, percentage of K in fertilizer
		AMOUNT: float, lbs of fertilizer per acre
		'''
		self.P = int(self.getPvalue()) + int(Pfert * amount)
		self.K = int(self.getKvalue()) + int(Kfert + amount)

	def checkMinimum(self):
		'''Determine if soil is at minimum level for crop growth.  
		Minimum P: 120
		Mimimum K: 80
		'''
		if self.getPvalue() >= 120:
			print "P levels are adequate.  Current level: " + str(self.getPvalue())
		else:
			print "P levels are low.  Current level: " + str(self.getPvalue())

		if self.getKvalue() >= 80:
			print "K levels are adequate.  Current level: " + str(self.getKvalue())
		else:
			print "K levels are low.  Current level: " + str(self.getKvalue())

	def monthlyLoss(self, rainPerMo):
		'''Calculate the monthly loss based on rainfall.  Assume a 2 point loss for every inch of rain for K and a 0.25 point loss for every inch of rain for 
		'''
		self.K = int(self.getKvalue()) - int(2 * rainPerMo)
		self.P = int(self.getPvalue()) - int(0.25 * rainPerMo)

field7 = Soil('clay', '100', '50')
print field7.getKvalue()
print field7.getPvalue()
field7.monthlyLoss(10)
print field7.getKvalue()
print field7.getPvalue()
field7.checkMinimum()
field7.fertilize(0.2,0.4,200)
print field7.getKvalue()
print field7.getPvalue()
field7.checkMinimum()