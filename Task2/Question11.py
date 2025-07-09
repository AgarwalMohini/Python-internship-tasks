# LCM and GCD

from math import gcd
a, b = map(int, input("Enter two integers: ").split())
g = gcd(a, b)

lcm = abs(a * b) // g   

print("GCD:", g)
print("LCM:", lcm)
