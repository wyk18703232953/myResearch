import random

def main(n):
    # 生成测试数据
    # n: 数组规模
    # q: 查询次数，这里设为 n，当然也可以根据需要调整
    q = n

    # 生成一个长度为 n 的随机数组，元素范围可自行调整
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 预生成 q 个随机查询区间 [l, r]，1-based
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原逻辑开始：统计初始逆序对奇偶性
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = (cnt % 2 == 0)

    # 处理查询
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

    # 输出结果
    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)