import random

def main(n):
    # 生成规模为 n 的测试数据
    # 假设键空间为 1..2n，值为 1..100
    keys1 = random.sample(range(1, 2 * n + 1), n) if n > 0 else []
    keys2 = random.sample(range(1, 2 * n + 1), n) if n > 0 else []

    d1 = {}
    for a in keys1:
        x = random.randint(1, 100)
        d1[a] = x

    d2 = {}
    for b in keys2:
        y = random.randint(1, 100)
        d2[b] = y

    ans = 0
    for key in set(d1.keys()) | set(d2.keys()):
        ans += max(d1.get(key, 0), d2.get(key, 0))

    print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)