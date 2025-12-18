n = int(input())
w = list(map(int, input().split()))
ent = input()
mp = {w[i]: i+1 for i in range(n)}
sorted(mp)
w.sort()
ptr = 0
stk = []
for i in range(2 * n):
    if ent[i] == "0":
        print(mp[w[ptr]], end=" ")
        stk.append(mp[w[ptr]])
        ptr += 1
    else:
        print(stk.pop(), end=" ")
    # print(pr.queue)
print()
