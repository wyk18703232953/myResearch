n,m = map(int,input().split())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
# arr3 = []
for first in arr1:
    for second in arr2:
        if first == second:
            # arr3.append(first)
            print(first,end=" ")