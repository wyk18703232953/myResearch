from sys import exit
n = int(input())
arr = [int(x) for x in input().split()]
tmp = 0
for i in range(len(arr)):
    tmp += (arr[i] - i)
arr.sort()
c = 0
for i in range(1, n):
    if arr[i] == arr[i - 1]:
        c += 1
    if i != 1 and arr[i] == arr[i - 1] and arr[i - 1] == arr[i - 2] + 1:
        print("cslnb")
        exit()
if c > 1 or (len(arr) >= 2 and arr[0] == arr[1] == 0):
    print("cslnb")
    exit()
print("cslnb" if tmp % 2 == 0 else "sjfnb")