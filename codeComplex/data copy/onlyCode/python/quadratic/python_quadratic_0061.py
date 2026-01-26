import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())

arr = [int(z) for z in input().split()]

q = int(input())

inv = 0

for i in range(n):

    for j in range(n):

        if i < j and arr[i] > arr[j]:

            inv += 1

        inv = inv % 2

for query in range(q):

    l, r = map(int, input().split())

    diff = r - l

    s = diff//2

    if diff % 2:
        s += 1

    inv = (inv + (s % 2)) % 2

    if inv:
        print("odd")
    else:
        print("even")

# for query in range(q):
#
#     l, r = map(int, input().split())
#
#     arr = arr[:l-1] + arr[l-1:r][::-1] + arr[r:]
#
#     inv = 0
#
#     for i in range(n):
#
#         inv += max(0, arr[i] - (i+1))
#
#     if inv % 2:
#         print("odd")
#     else:
#         print("even")
#
#     print(inv)

