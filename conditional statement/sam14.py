"""wap to take two num from user enter your choice if 1 then addition if 2 then substraction if 3 multiplication if 4 then invalid"""
choice=int(input("enter your choice="))
num1=int(input("enter first num="))
num2=int(input("enter second num="))

match choice:
    case 1:print(num1+num2)
	case 2:print(num1-num2)
	case 3:print(num1*num2)
	case _:print("invalid")

