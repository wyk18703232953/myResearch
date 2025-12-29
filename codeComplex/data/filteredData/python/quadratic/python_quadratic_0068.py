import random

def main(n):
    # 生成测试数据
    # 数组 a 的长度为 n，元素为 0~n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    # 生成若干查询，这里设为 n 次查询
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原逻辑开始
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    for l, r in queries:
        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            print('even')
        else:
            print('odd')