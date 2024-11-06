n=int(input("enter the number of elements"))
numbers=[]
for i in range(n):
    x=int(input("enter the no:"))
    numbers.append(x)
print(numbers)
while True:
    print("\n Menu")
    print("\n 1. find the greatest and the lowest no")
    print("\n 2. sort the list in ascending order")
    print("\n 3. create a list of even numbers")
    print("\n 4. exit")

    choice=input("enter your choice:")
    if choice=='1':
        print("greatest no:",max(numbers))
        print("lowest number:",min(numbers))
    elif choice=='2':
        print("sorted list:",sorted (numbers))
    elif choice=='3':
        even_numbers=[]
        for num in numbers:
            if num%2==0:
                even_numbers.append(num)
        print("list of even numbers:",even_numbers)
    elif choice=='4':
        print("exiting the program")
        break
    else:
         print("invalid choice")
          
