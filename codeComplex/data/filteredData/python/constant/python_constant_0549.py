import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里设 s 为 [1, n^2] 区间内的随机整数，避免过大数字
    if n <= 0:
        raise ValueError("n 必须为正整数")

    s = random.randint(1, n * n)

    # 原逻辑：计算将 s 分成若干份、每份最多 n 时需要的份数
    if s <= n:
        sol = 1
    else:
        sol = s // n
        if s % n:
            sol += 1

    print(sol)

if __name__ == "__main__":
    # 示例：可以在此处调用 main 进行简单测试
    main(10)