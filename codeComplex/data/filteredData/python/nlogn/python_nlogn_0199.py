from collections import Counter
import random

def main(n: int):
    # 生成规模为 n 的测试数据，元素范围可根据需要调整
    # 这里设为 [-10**5, 10**5]
    arr = [random.randint(-10**5, 10**5) for _ in range(n)]

    mp = Counter()
    tot, cnt, ans = 0, 0, 0

    for i in arr:
        ncnt = cnt - mp[i] - mp[i + 1] - mp[i - 1]
        ntot = tot - (i * mp[i]) - ((i - 1) * mp[i - 1]) - ((i + 1) * mp[i + 1])
        nsum = (ncnt * i) - ntot
        ans += nsum
        mp[i] += 1
        cnt += 1
        tot += i

    print(ans)


if __name__ == "__main__":
    # 示范调用，可修改 n 测试不同规模
    main(10)