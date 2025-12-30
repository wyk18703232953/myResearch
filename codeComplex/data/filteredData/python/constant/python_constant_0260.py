import random

def main(n: int) -> None:
    # 生成测试数据：
    # n: 给定规模
    # pos: 1..n
    # l, r: 1 <= l <= r <= n
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)  # 保证 l <= r

    # 原逻辑开始
    if l == 1 and r == n:
        ans = 0
    else:
        if l != 1 and r != n:
            ans = min(abs(l - pos), abs(r - pos)) + 2 + abs(r - l)
        else:
            if l == 1:
                ans = abs(pos - r) + 1
            else:
                ans = abs(pos - l) + 1

    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的规模
    main(10)