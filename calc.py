a=int(input("""

               Press 1 for addition
               Press 2 for subtraction
               Press 3 for division
               Press 4 for multiplication
            """))
c=int(input("num1"))
d=int(input("num2"))
if(a==1):
    print(c+d)
elif(a==2):
    print(c-d)
elif(a==3):
    print(c/d)
elif(a==4):
    print(c*d)
else:
    print("there is no operation exixts")

