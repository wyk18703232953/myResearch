rgb = 'RGB' * 1000
for q in range(int(input())):
    n, k = [int(s) for s in input().split()]
    s = input()
    ans = 3000
    for w in range(3):
        for e in range(n - k + 1):
            temp = 0
            for i in range(k):
                if s[e + i] != rgb[w + i]:
                    temp += 1
            ans = min(ans, temp)
    print(ans)