n=int(input("enter the number of terms:"))
a=0
b=1
print("fibanacci series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
