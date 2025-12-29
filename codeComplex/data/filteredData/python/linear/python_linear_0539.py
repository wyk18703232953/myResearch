import random

def solve(slimes):
    if len(slimes) == 1:
        return slimes[0]

    havePos = False
    haveNeg = False

    for s in slimes:
        if s > 0:
            havePos = True
        elif s < 0:
            haveNeg = True

    if havePos and haveNeg:
        return sum(map(abs, slimes))
    elif not havePos:
        m = max(slimes)
        return sum(map(abs, slimes)) + 2 * m
    elif not haveNeg:
        m = min(slimes)
        return sum(map(abs, slimes)) - 2 * m
    else:
        return 0

def main(n):
    # 生成规模为 n 的测试数据，这里使用 [-10^9, 10^9] 范围内的随机整数
    slimes = [random.randint(-10**9, 10**9) for _ in range(n)]
    ans = solve(slimes)
    print(ans)