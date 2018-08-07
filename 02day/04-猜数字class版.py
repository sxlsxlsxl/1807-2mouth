class game:
	def jsb(self):

		import random
		while True:
			c = random.randint(1,3)#电脑随机出数
			print("1—石头".center(50))
			print("2—剪刀".center(50))
			print("3—布".center(50))
			p = int(input("请选择:"))#玩家输入
			if c == p:
				print("平局")
			elif (c == 1 and p == 2) or (c == 2 and p == 3) or (c == 3 and p == 1):
				print("弱爆了")
			else:
				print("厉害了")

a = game()
a.jsb()
