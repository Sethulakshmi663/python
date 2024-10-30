n=["3","5","6","4"]
print("list before swapping:",n)
length=len(n)
temp=n[0]
n[0]=n[length-1]
n[length-1]=temp
print("list after swapping:",n)
