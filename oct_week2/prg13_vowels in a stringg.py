sentence=input("enter the sentence:")
string=sentence.lower()
print(string)
count=0
list1=["a","e","i","o","U"]
for char in string:
    if char in list1:
        count=count+1
print("number of vowels in given sentenceis:",count)
        
