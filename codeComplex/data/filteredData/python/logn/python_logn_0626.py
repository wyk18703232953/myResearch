import random

def main(n):
    # 生成测试数据：随机选择 1 <= m <= n*(n+1)//2
    max_sum = n * (n + 1) // 2
    if max_sum == 0:
        return  # n<=0 时直接返回
    m = random.randint(1, max_sum)

    # 原逻辑开始
    for i in range(1, n + 1):
        j = i * (i + 1) // 2
        if j >= m:
            if j == m and i == n:
                print(0)
                break
            else:
                t = n - i
                if j - t == m:
                    print(t)
                    break
                elif j - t < m:
                    continue


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)