import random

def main(n):
    # 随机生成一个满足题意的 k（这里简单设为 1..n 之间的整数）
    # 若有更明确的生成规则，可按题意修改
    if n <= 0:
        return  # 或者 raise ValueError("n must be positive")
    k = random.randint(1, n)

    # 以下为原逻辑（去除 input()，用参数 n 和生成的 k）
    if n == 1:
        print(0)
    elif n - 1 > (1 + k - 1) * (k - 1) // 2:
        print(-1)
    else:
        n -= 1
        k -= 1
        l, r = 0, k + 1
        while r - l > 1:
            m = (l + r) // 2
            if (m + k) * (k - m + 1) // 2 >= n:
                l = m
            else:
                r = m
        print(k - l + 1)

# 示例调用（提交到评测系统时可删除）
if __name__ == "__main__":
    main(10)