"""wap to take two num from user enter your choice if 1 then addition if 2 then substraction if 3 multiplication if 4 then invalid"""
choice=int(input("enter your choice"))
num1=int(input("enter first num="))
num2=int(input("enter second num="))

if choice==1:
	add=num1+num2
	print(add)
elif choice==2:
	sub=num1-num2
	print(sub)
elif choice==3:
	multi=num1*num2
	print(multi)
else:
	print("invalid num")