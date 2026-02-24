"""wap take emp salary from keyboard if salary>=5000 da=30% hr=20%
then display basic salary da hr and total salary """
sal=int(input("enter basic salary="))

da=sal*0.3 if sal>=5000 else sal*0.2
hr=sal*0.2 if sal>=5000 else sal*0.1
print("da=",da)
print("hr=",hr)




