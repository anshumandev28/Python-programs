total_class = 50
name = input("enter the name:")
att=int(input("enter the atten class:"))
p = (att/total_class)*100
if(p>=75):
    print(name,"eligible for test")
else:
    print(name,"Not eligible for test")

def atten(att,total):
     name=input("enter the name:")

     p=(att/total_class)*100
     if (p>=75):
         print(name,"eligible for test")
     else:
         print(name,"not eligible for test")

x=40
y=50

atten(x,y)
