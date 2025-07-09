# Sum of digits

n=int(input("Enter an integer: "))
sum1=0
while(n>0):
    rem=n%10
    sum1+=rem
    n=n//10
print("Sum of digits is:", sum1)