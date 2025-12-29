from collections import defaultdict
import random

def main(n):
    # 生成测试数据
    # 约定：k 为 1~10^9 的随机整数（不为 0），
    #       数组 a 中元素为 1~10^9 的随机整数
    k = random.randint(1, 10**9)
    a = [random.randint(1, 10**9) for _ in range(n)]

    cnt = [defaultdict(lambda: 0) for _ in range(11)]
    for i in a:
        cnt[len(str(i))][i % k] += 1

    ans = 0
    d = 10
    for i in range(1, 11):
        cnti = cnt[i]
        for j in a:
            ans += cnti[(k - d * j) % k]
        d *= 10

    for i in a:
        if int(str(i) * 2) % k == 0:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(5)