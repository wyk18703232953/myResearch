from itertools import combinations
import random

def main(n: int) -> int:
    # 生成测试数据
    # a 为长度为 n 的题目难度数组，取值 1~1000
    a = [random.randint(1, 1000) for _ in range(n)]
    # 生成约束参数：l, r, x
    total_sum = sum(a)
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum if total_sum > 0 else l)
    x = random.randint(0, max(a) - min(a) if n > 1 else 0)

    ans = 0
    for i in range(2, n + 1):
        for p in combinations(a, i):
            if l <= sum(p) <= r and max(p) - min(p) >= x:
                ans += 1
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)