from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 约束条件可根据需要调整，这里给出一种合理的生成方式
    # l 和 r 为总和下界和上界，x 为最大值和最小值的差的下界
    a = [random.randint(1, 100) for _ in range(n)]
    l = n * 10           # 下界
    r = n * 50           # 上界
    x = max(1, n // 5)   # 差值下界

    ans = 0
    for i in range(2, n + 1):
        for j in combinations(a, i):
            if max(j) - min(j) >= x and l <= sum(j) <= r:
                ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 可自行调整
    main(5)