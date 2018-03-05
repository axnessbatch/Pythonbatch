n=151
sum=0
while n>0:
    rem=n%10
    sum+=rem**3
    n=n//10
if sum == n:
    print(n,'is armsrong number')
else:
    print(n,'is armsrong not number')
