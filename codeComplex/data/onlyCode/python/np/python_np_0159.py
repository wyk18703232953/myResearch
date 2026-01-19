# B. Preparing Olympiad

def check_combination(v):
    sm = sum(v)
    if l <= sm <= r:
        if max(v) - min(v) >= x:
            global ans
            ans += 1


def go(offset, k):
    # https://stackoverflow.com/questions/12991758/creating-all-possible-k-combinations-of-n-items-in-c/28698654
    if k == 0:
        check_combination(combination)
        return
    for i in range(offset, len(problems) - k + 1):
        combination.append(problems[i])
        go(i+1, k-1)
        combination.pop()


n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))

problems = list()
combination = list()

ans = 0

for i in range(2, len(c) + 1):
    problems = c.copy()
    go(0, i)

print(ans)
