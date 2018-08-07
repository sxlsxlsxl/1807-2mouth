class car():
	def __init__(self,name,color,type):
		self.name = name
		self.color = color
		self.type = type
	def run(self):
		print("200km/s")
	def chexing(self):
		print("颜色是%s，车型是%s"%(self.color,self.type))
	def lision(self):
		print("DJ舞曲")

aodi = car("奥迪","白色","Q8")
aodi.run()
aodi.chexing()
aodi.lision()
