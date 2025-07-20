#Swap two numbers

a = int(input())
b = int(input())

# Swapping without third variable using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
