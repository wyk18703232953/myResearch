from itertools import permutations

n = int(input())
a = []
for i in range(4):
    a.append([list(map(int, list(input()))) for j in range(n)])
    if i < 3:
        input()

ans = 10 ** 10
for i in permutations(a, 4):
    cnt = 0
    total = 0
    for j in i:
        if cnt < 2:
            cnt2 = 0
            for p in j:
                for q in p:
                    if q != cnt2 % 2:
                        total += 1
                    cnt2 += 1
        else:
            cnt2 = 1
            for p in j:
                for q in p:
                    if q != cnt2 % 2:
                        total += 1
                    cnt2 += 1
        cnt += 1

    ans = min(ans, total)

print(ans)