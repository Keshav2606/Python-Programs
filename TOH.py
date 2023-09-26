def TOH(n, x, y, z):
    if (n > 0):
        TOH(n-1, x, z, y)
        print(x, "->", z)
        TOH(n-1, y, x, z)


n = int(input("Enter the number of disks:"))
TOH(n, 'A', 'B', 'C')
