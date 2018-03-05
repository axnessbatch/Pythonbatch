a=input('enter the first number')
b=input('enter the second number')
c=input ('enter third number')
d=input('enter fourth number')

if(a<b and a<c and a<d):
    print("a is small")
elif(b<c and b<d):
    print("b is small")
elif(c<d):
    print("c is small")
else :
    print('d is small')
