# Q-2(a)

# def removekth(str, k):
#     if k >= 0:
#         return str[:k] + str[k+1:]


# print(removekth("PYTHON", 1))
# print(removekth("PYTHON", 3))
# print(removekth("PYTHON", 0))
# print(removekth("PYTHON", 20))

# Q-2(b)


# def average(list):
#     sum = 0
#     count = 0
#     for i in list:
#         sum = sum + i
#         count += 1
#     avg = sum/count
#     return avg


# try:
#     list = [1, 2, 11, 12, 15]
#     print(average(list))
# except ZeroDivisionError:
#     print("Error: List is Empty")


# Q-2(d)


# def lessthan(lst, k):
#     return [i for i in lst if i < k]


# lst = [1, -2, 0, 5, -3]
# print(lessthan(lst, 0))

# Q-2(e)


# def factors(n):
#     return [i for i in range(1, n+1) if n % i == 0]


# print(factors(6))
# print(factors(1))
# print(factors(13))

# Q-4(a)

# def makePairs(list1, list2):
#     n = len(list1)
#     return [(list1[i], list2[i]) for i in range(n)]


# list1 = [0, 2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 9]
# print(makePairs(list1, list2))

# Q-6(b)

# from math import sqrt


# def countSquares(n):
#     if n == 1:
#         print("ONLY 1 is a perfect square <= 1")
#     else:
#         num = 1
#         while num <= sqrt(n):
#             square = num**2
#             num += 1
#             print(square, end=", ")
#         print("are the perfect squares <= ", n)


# n = int(input("Enter the Number: "))
# countSquares(n)


# Q-7(a)

def alternating(lst):
    if lst[0] % 2 != 0:
        return False

    for i in range(1, len(lst), 2):
        if lst[i] % 2 != 1:
            return False
        if lst[i-1] % 2 != 0:
            return False
    return True


lst = [10, 1, 12, 3, 4, 52]
print(alternating(lst))


# Q-7(b)

# def searchMany(s, x, k):
#     if k > 0:
#         count = 0
#         for i in s:
#             if i == x:
#                 count += 1
#         if count <= k:
#             return True
#         else:
#             return False


# s = [10, 11, 10, 12, 15, 15, 12, 10]
# x = int(input("Enter the Element to search: "))
# k = int(input("Enter the atmost occurence: "))
# print(searchMany(s, x, k))
