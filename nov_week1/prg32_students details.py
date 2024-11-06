student={
'name':input("enter the students name:"),
'roll no':input("enter students roll no:"),
'reg no':input("enter students reg no:"),
'dept':input("enter students department:"),
'sem':input("enter students semester:"),
}
print("entered students details:",student)
total_mark=int(input("enter the students total mark:"))
student['total_mark']=total_mark
if total_mark>=90:
    grade='A'
elif total_mark>=82:
    grade='B'    
elif total_mark>=75:
    grade='C'
elif total_mark>=60:
    grade='D'
elif total_mark>=50:
    grade='pass'
else:
    grade='F'
student['grade']=grade
print("\n updated students details:",student)
del student['roll no']
print("\n students details after deletion:",student)

