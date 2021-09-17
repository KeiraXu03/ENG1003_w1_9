print("This is ENG1003 Week1 Tutorial Programming Task")
g=input("enter the function  number to be executed:")
def put1():
    print("jason ")
    print("XU ZHUONING ")
    print("HUYUXIN ")
    print("MAT")
    print("Asaad ARSHAD")
def put2():
    a=5
    b=7
    c=9
    Sum=a+b+c
    print("a = ",a," b = ",b," c = ",c ,"  Sum = ",Sum)
def put3():
    a=5
    print("a = ",a," , ","Square of a: ",a*a)
def put4():
    a=5
    b=4
    if a>b:
        print(a,"is larger than ",b)
    else:
        print(b,"is larger than ",a)
if int(g) == 1:
  put1()
elif int(g) == 2:
  put2()
elif int(g) == 3:
  put3()
elif int(g)==4:
  put4()
