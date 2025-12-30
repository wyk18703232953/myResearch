from collections import Counter
import random

def main(n):
    # 1. 生成规模为 n 的测试数据：由 's','p','m' 三种花色，1~9 牌号组成
    suits = ['s', 'p', 'm']
    tiles = []
    for _ in range(n):
        s = random.choice(suits)
        r = random.randint(1, 9)
        tiles.append(s + str(r))

    # 2. 将原程序逻辑封装
    ts = Counter(''.join(reversed(t)) for t in tiles)
    t0 = None
    run = 0
    ans = 3
    for t, c in sorted(ts.items()):
        if t0 is None or t[0] != t0[0] or int(t[1]) != int(t0[1]) + 1:
            run = 0
        t0 = t
        run += 1
        ans = min(ans, 3 - max(c, run))
    for s in 'spm':
        for r in range(1, 10):
            if s + str(r - 1) in ts and s + str(r + 1) in ts:
                ans = min(ans, 1)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(20)
    main(20)