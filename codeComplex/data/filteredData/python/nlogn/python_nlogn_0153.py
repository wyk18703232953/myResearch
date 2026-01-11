def func(k, a):
    if len(a) == 1:
        return 1
    if k == 1:
        return len(a)
    s = set(a)
    for x in sorted(a):
        if x in s and k * x in s:
            s.remove(k * x)
    return len(s)


def main(n):
    # 映射规则：
    # n: 数组长度
    # k: 从 n 导出，保证确定性且避免退化为 k=1 的特殊情况
    if n <= 0:
        return 0
    # 确定性生成 k（避免 k=1 的分支，以便更贴近一般情况）
    k = (n % 5) + 2  # k ∈ {2,3,4,5,6}
    # 确定性生成数组 a，长度为 n
    # 构造包含重复因子关系的数组以激活核心逻辑：
    # a[i] = (i + 1) * ((i // 3) % 4 + 1)
    a = [(i + 1) * ((i // 3) % 4 + 1) for i in range(n)]
    return func(k, a)


if __name__ == "__main__":
    # 示例调用：可根据需要调整 n
    result = main(10)
    # print(result)
    pass