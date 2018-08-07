class person:
	def run(self):
		print("跑")
	def eat(self):
		print("吃饭")
	def sleep(self):
		print("睡觉")
	def introduce(self):
		print("我是%s,我今年%d岁"%(self.name,self.age))

#sxl.name = "石现龙"
#sxl.age = 17
sxl = person()
sxl.run()
sxl.eat()
sxl.sleep()
sxl.name = "石现龙"
sxl.age = 17
sxl.introduce()
print(sxl.name)
print(sxl.age)
