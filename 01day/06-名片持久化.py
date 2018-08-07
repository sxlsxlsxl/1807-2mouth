'''
list = [{"name":"老王","age":20},{"name":"小元","age":15}]

f = open("3-名片持久化.data","w")
f.write(str(list))
f.close()
'''
'''
list = []
f_1 = open("3-名片持久化.data","r")
i = f_1.read()
list = eval(i)
if len(i) != 0:
for i in list:
	for k,v in i.items():
		print(k,v)
print(list)
f_1.close()
'''


list = []
#dict = {}
print("欢迎来到名片系统——管理员")
while True:
	list_1 = []
	dict = {}
	print("1—添加".center(50))
	print("2—删除".center(50))
	print("3—修改".center(50))
	print("4—查看".center(50))
	print("0—退出".center(50))
	a = int(input("请选择:"))
	if a == 1:
		name = input("请输入名字:")
		age = int(input("请输入年龄:"))
		dict["name"] = name
		dict["age"] = age
		list_1.append(dict)
		list.append(list_1)
		print(list)
		f = open("4-名片持久化副本.data","a+")
		f.write(str(list_1))
		f.close()
	elif a == 2:
		pass
	elif a == 3:
		pass
	elif a == 4:
		pass
	elif a == 0:
		exit()

	

