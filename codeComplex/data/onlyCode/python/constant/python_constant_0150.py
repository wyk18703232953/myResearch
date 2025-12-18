# n = int(input())
# digits = list([])
# new_digits= set({})
# for i in range(n):
#     n = int(input())
#     if n in range(1,10):
#         print(1)
#         print(n)
#     else:
#         while n > 0 :
#             digit = n % 10
#             digits.append(digit)
#             n = int(n /10)
#         i = 0
#         for d in digits:
#             new_digits.add(d * 10**i)
#             i += 1
#         if 0 in new_digits:
#              new_digits.remove(0)
#         print(len(new_digits))
#         for d in new_digits:
#             print(d,end=" ")
#         print('')
#         new_digits.clear()
#         digits.clear()

# we need to find the index of these values in the given array
# n = int(input())
# a = list(map(int,input().split(' ')))
# b = list([])
# for i in range(1,n+1):
#     b.append(i)
# results = []
# for l in b:
#     results.append(a.index(l) + 1)
#
# for r in results:
#     print(r,end=" ")


# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# d = int(input())
# nums = list([])
# for i in range(1,d+1):
#     nums.append(i)
# results = set({})
# for num in nums:
#     if num % k == 0 :
#         results.add(num)
#     elif num % l == 0 :
#         results.add(num)
#     elif num % m == 0 :
#         results.add(num)
#     elif num % n == 0 :
#         results.add(num)
# print(len(results))

# function problem
# n = int(input())
# result = 0
#
# if n %2 == 0:
#     result = int(n /2)
# else:
#     result = -1 * (int(n / 2) + 1)
# print(result)




# General arrival
# n = int(input())
# a = list(map(int,input().split(' ')))
# b = list(dict.fromkeys(a))
# finding the max number and index
# max_index = 0
# i = 0
# maxi = a[0]
# while i < len(b):
#     if b[i] >= maxi:
#         maxi = b[i]
#         max_index = i
#     i += 1

# finding the min number and index
# min_index = 0
# i = 0
# mini = max(b)
# while i < len(b):
#     if b[i] <= mini:
#         mini = b[i]
#         min_index = i
#     i += 1
# if len(a) == 2:
#     print(len(a) - 1)
# else:
#     print( (max_index - 0) + ((len(b) - 1) - min_index) )
# print(b)



def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               return  False
        else:
            return True
    else:
        return False

n = int(input())
temp = 0
first = 0
second = 0
if n % 2 == 0:
    temp = int(n/2)
    first = temp
    second = n - temp
    while is_prime(first) or is_prime(second):
        first -= 1
        second += 1
        if first + second == n and (not is_prime(first) and not is_prime(second)):
            break
else:
    temp = int(n / 2)
    first = temp
    second = n - first
    while is_prime(first) or is_prime(second):
        first -= 1
        second += 1
        if first + second == n and (not is_prime(first) and not is_prime(second)):
            break
print(first,end=" ")
print(second)