fib = [0]*100
fib[1] = 1
for i in range(2, 100):
    fib[i] = fib[i-1] + fib[i-2]
# ans = [fib[0], fib[1], fib[2]]
# i = 3
# j = 0
n = int(input())
# print(fib)
# ok = False
if (n in fib):
    if (n == 0):
        print(0, 0, 0)
    elif (n == 1):
        print(0, 0, 1)
    else:
        print(0, fib[fib.index(n)-2], fib[fib.index(n)-1])
else:
    print("I'm too stupid to solve this problem")
# while True:
#     if (sum(ans) == n):
#         ok = True
#         break
#     else:
#         if (j == 1):
#             j = 0
#         ans[j] = fib[i]
#         print(i)
#         j += 1
#         i += 1
# if (ok):
#     print(*ans)
# else:
#     print("I'm too stupid to solve this problem")