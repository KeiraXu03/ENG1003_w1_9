import random
def put1(height):
    height2=0
    while(height2<height):
        print("XXX")
        height2=height2+1
def put2(first,second):
    print("The sum is:",first+second)
def put3(length):
    length0=0
    length2=length
    while(length0<length):
        print(length2)
        length0=length0+1
        length2=length2-1
def put4(size0):
    size1=0
    size2=0
    while(size1<size0):
        while(size2<size0-1):
            print("[]",end="")
            size2+=1  
        print("[]")    
        size1+=1
        size2=0
def put5():
    a2=int(random.randint(1,200))
    b=int(random.randint(1,a2))
    print("Number Guessing Game")
    print("The range for this round is 1 -",a2)
    c=int(1)
    d=int(1)
    up=a2
    down=int(1)
    while(c!=b):
      d+=1
      c=int(input("Make a Guess:"))
      if(c>b):
          print("The range is now ",down,"-",c,end="!")
          print("\n")
          up=c
      elif(c<b):
          print("The range is now",c,"-",up,end="!")
          down=c
          print("\n")
      elif(c==b):
          print("BINGO! , You took",d-1,"attempts to reach the answer")
print("This is ENG1003 Week1 Tutorial Programming Task")
g=int(1)
while(g==1 or g==2 or g==3 or g==4 or g==5):
     g=int(input("enter the function  number to be executed:"))
     import random  
     if int(g) == 1:
        height1=int(input("height:"))
        put1(height1)
     elif int(g) == 2:
        first1=int(input("First number:"))
        second1=int(input("Second number:"))
        put2(first1,second1)
     elif int(g) == 3:
        length1=int(input("List length:"))
        put3(length1)
     elif int(g)==4:
        size=int(input("Square size:"))
        put4(size)
     elif int(g)==5:
        put5()
     elif (g!=1 and g!=2 and g!=3 and g!=4 and g!=5):
        print("wrong  number!")
