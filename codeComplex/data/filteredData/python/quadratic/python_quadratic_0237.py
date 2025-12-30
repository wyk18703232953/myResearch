import bisect
import random

def main(n: int):
    # 生成测试数据：随机生成 s 和 c
    # s 为 1~10^9 之间的互不相同整数，c 为 1~10^9 之间的整数
    # 根据需要可调整随机种子或生成规则
    random.seed(0)
    s = random.sample(range(1, 10**9), n)
    c = [random.randint(1, 10**9) for _ in range(n)]

    ans = 10**18
    for mid in range(1, n - 1):
        l1 = [c[i] for i in range(mid) if s[i] < s[mid]] + [10**18]
        l2 = [c[i] for i in range(mid + 1, n) if s[i] > s[mid]] + [10**18]
        ans = min(ans, min(l1) + c[mid] + min(l2))
    if ans >= 10**18:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)