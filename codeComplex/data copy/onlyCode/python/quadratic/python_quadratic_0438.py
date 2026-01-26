n = int(input())

arr = [int(z) for z in list(input())]
ans = 0

if n == 2:
    if arr[0] == arr[1]:
        print("YES")
    else:
        print("NO")
    exit()

for l in range(1, n-1):
    s = sum(arr[:l])
    i = l
    v = [s]
    curr = 0
    while i < n:
        curr += arr[i]
        if i == n-1:
            if curr > s:
                curr -= arr[i]
                v.append(curr)
                curr = arr[i]
            v.append(curr)
        elif curr > s:
            curr -= arr[i]
            v.append(curr)
            curr = arr[i]
        i += 1

    #print(v)

    if len(set(v)) == 1:
        print("YES")
        #print(l, s, v)
        ans = 1
        exit()

if not ans:
    print("NO")


#
# ans = 0
# for p in range(sum(arr)+1):
#     i = 0
#     curr = 0
#     while i < n:
#         if i == n-1:
#             if curr+arr[i] != p:
#                 break
#             else:
#                 print("YES")
#                 ans = 1
#                 exit()
#         curr += arr[i]
#         if curr == p:
#             if i == n-1:
#                 i += 1
#             i += 1
#             curr = 0
#             continue
#         elif curr > p:
#             break
#         elif curr < p:
#             i += 1
#
#     if i == n:
#         print("YES")
#         ans = 1
#         exit()
#     #print(p)
#
# if not ans:
#     print("NO")