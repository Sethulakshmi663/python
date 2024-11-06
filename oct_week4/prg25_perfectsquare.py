import math
start=int(input("enter the start of the range:"))
end=int(input("enter enf of the range:"))
result=[]
for i in range(int(math.sqrt(start)),int(math.sqrt(end))+1):
    square=i*i
    if 1000<=square<=9999:
        if all(int(digit)%2==0 for digit in str(square)):
            result.append(square)
if result:
    print("four digits perfect square with all even digits",result)
else:
    print("no four digits perfect square with all even digits found") 
