import random

def main(n: int):
    # 生成测试数据：
    # n 已由参数给出
    # pos, l, r 满足 1 <= l <= r <= n 且 1 <= pos <= n
    l = random.randint(1, n)
    r = random.randint(l, n)      # 保证 l <= r
    pos = random.randint(1, n)

    # 原逻辑
    if l == 1 and r == n:
        ans = 0
    elif l == 1:
        ans = abs(pos - r) + 1
    elif r == n:
        ans = abs(pos - l) + 1
    else:
        ans = min(abs(pos - l), abs(pos - r)) + abs(l - r) + 2

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可按需调整
    main(10)