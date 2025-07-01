# To check if a number is an Armstrong number or not

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if equal to the original number
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
