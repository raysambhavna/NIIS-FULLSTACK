#wap to check num is sd,dd,td or od or zero
num=int(input("enter a num="))

if num>10 and num<100:
	print("num is double digit number")
elif num>0 and num<10:
	print("num is single digit number")
elif num>99 and num<1000:
	print("num is triple digit number")
else:
	print("num is -ve")



