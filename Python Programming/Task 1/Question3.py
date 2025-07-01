#To calculate the factorial of a number

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n* fact(n-1)
n=int(input())
result=fact(n)
print("The factorial of the number is: ",result)