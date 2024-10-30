list1=(input("enter the 1st list separated by spaces:")).split()
list2=(input("enter the 2nd list separated by spaces:")).split()
for i in range(len(list1)):
        list1[i]=int(list1[i])
for i in range(len(list2)):
        list2[i]=int(list2[i])
if(len(list1)==len(list2)):
    print("the list are of the same length")
else:
    print("the list are of different length")
if(sum(list1)==sum(list2)):
    print("list sum to same value")
else:
    print("list sum to different value")
common_value=set(list1)&set(list2)
if common_value:
    print("common_values",common_value)
else:
    print("no common_value")
   
               
