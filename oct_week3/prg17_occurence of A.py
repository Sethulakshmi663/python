string=input(" enter the sentence:")
count=0
for item in string:
    count+=item.lower().count('a')
print("no of times 'a' appear is:",count)
