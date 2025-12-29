import random

def main(n: int):
    # 生成测试数据
    # m 在原代码中未实际使用，这里仍生成以保持结构一致
    m = random.randint(1, max(1, n))  # 仅示例用
    # 生成长度为 n 的数组 a，元素为 1 到 10^6 的随机整数
    a = [random.randint(1, 10**6) for _ in range(n)]

    # 原始逻辑开始（去除 input，并用生成的数据替代）
    h = max(a)
    a.sort()
    a.reverse()
    a.append(0)
    ans = sum(a)
    for i in range(n):
        if a[i + 1] >= a[i]:
            a[i + 1] = a[i] - 1
        ans -= max(a[i] - a[i + 1], 1)

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(10)