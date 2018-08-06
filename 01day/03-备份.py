name = input("请输入您要备份的文件名(要加后缀名)")

f = open(name,"r")
a = f.read()

f1 = open("2.txt","w")
f1.write(a)

f.close()
f1.close()
