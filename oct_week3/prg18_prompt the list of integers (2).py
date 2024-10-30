list=int(input("enter the number of integers to input:"))
length=[]
for i in range(list):
    integer=int(input("enter the number of integers"))
    length.append(integer)
    if(integer>100):
        length[i]="over"
print(length)
