class Driver:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.win = 0

	def winRace(self):
		self.win += 1

	def show(self):
		return (self.name,self.age)

x = Driver("Ash",19)
y = Driver("Likhi",17)
z = Driver("Jwow",24)
L = [x,y,z]
print L
# x= Driver(eval(raw_input( "Enter Driver (name,age): ")))
# L=[]
# L.append(x)
# while bool(x):
# 	x = raw_input( "Enter Driver (name,age): ")
# 	if x:
# 		L.append(Driver(eval(x)))
# print L

# for driver in L:
# 	(name,age) = driver.show()
# 	if name == 'Jwow':
# 		driver.winRace()
# 		driver.winRace()
# 	elif name == "Ash":
# 		driver.winRace()
# 		driver.winRace()


wins = {}


print wins
while 1:
	n = raw_input("Next Winner: ")
	for driver in L:
		(name,age) = driver.show()
		if name == n:
			driver.winRace()
	for driver in L:
		(name,age) = driver.show()
		try:
			if name not in wins[driver.win]:
				if not wins[driver.win]:
					wins[driver.win] = [name]
				else:
					wins[driver.win].append(name)
     				if driver.win > 0:
						wins[driver.win-1].remove(name)
		except KeyError:
			wins[driver.win] = [name]
			if driver.win > 0 and name in wins[driver.win-1]:
				wins[driver.win-1].remove(name)
	print wins
