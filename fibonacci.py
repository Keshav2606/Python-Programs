def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


def is_fibonacci(n):
    n1 = 0
    n2 = 1
    while n2 < n:
        n3 = n1+n2
        n1 = n2
        n2 = n3
    return (n3 == n or n == 0)


n = int(input("Enter the Number:"))
for i in range(n):
    print(fibonacci(i))

print(is_fibonacci(n))
