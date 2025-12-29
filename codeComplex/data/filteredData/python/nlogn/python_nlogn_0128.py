import random

def main(n):
    # 生成测试数据
    # 约束：1 <= m <= n，k 为非负，a[i] 为非负
    m = random.randint(1, n)          # 目标值
    k = random.randint(0, n)          # 额外可加总量
    a = [random.randint(0, n) for _ in range(n)]  # 原数组

    # 原始逻辑开始
    a.sort(reverse=True)

    if sum(a) + k - n < m:
        print(-1)
    elif k >= m:
        print(0)
    else:
        for i in range(1, n + 1):
            if sum(a[:i]) + k - i >= m:
                print(i)
                break

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)