#To return a fibonacci sequence

def fib_sequence(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter the number of terms: "))
result = fib_sequence(n)
print("Fibonacci sequence up to", n, "terms:", result)
