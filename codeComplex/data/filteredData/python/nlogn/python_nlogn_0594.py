import random

def main(n):
    # 生成测试数据：k 和数组 a
    # 这里不使用 k（原代码亦未使用），仅保持结构一致
    k = random.randint(1, max(1, n))
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 原逻辑开始
    a.sort(reverse=True)
    worst = 0
    maxi = a[0]
    a.append(0)
    for i in range(n + 1):
        bad = maxi - a[i] - i
        worst = max(worst, bad)
    result = sum(a) - n - worst
    print(result)
    return result

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)