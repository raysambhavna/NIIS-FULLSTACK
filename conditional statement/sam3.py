"""wap take emp salary from keyboard if salary>=5000 da=30% hr=20%
then display basic salary da hr and total salary """
sal=int(input("enter basic salary="))
da=0
hr=0
if sal>=5000:
	da=sal*30/100
	hr=sal*20/100

totalsal=hr+da
print("basic salary",sal)
print("DA=",da)
print("HR=",hr)
print("totalsal=",totalsal)




