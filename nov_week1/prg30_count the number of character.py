string=input("enter the string:")
for i in string:
    frequency=string.count(i)
    print(str(i)+":"+str(frequency),end=",")
