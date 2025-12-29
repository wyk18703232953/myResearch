import random

def main(n):
    # 生成测试数据
    # 生成长度为 n 的数组 a，元素范围可按需调整
    a = [random.randint(0, 100) for _ in range(n)]

    # 生成查询数量 q 和对应区间 [l, r]
    q = max(1, n // 2)
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原始逻辑开始（移除 input()，使用生成的数据）

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = (cnt % 2 == 0)

    ans = []
    for l, r in queries:
        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            ans.append('even')
        else:
            ans.append('odd')

    print('\n'.join(ans))


# 示例调用
if __name__ == "__main__":
    main(5)