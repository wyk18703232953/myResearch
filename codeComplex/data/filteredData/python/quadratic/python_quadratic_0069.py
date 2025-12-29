import random

def main(n: int):
    # 生成测试数据
    # 生成长度为 n 的数组 a，元素为 1 到 n 的随机整数
    a = [random.randint(1, n) for _ in range(n)]

    # 生成随机查询数量 q（这里设为 n，按需要可调整）
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(1, n)
        if l > r:
            l, r = r, l
        queries.append((l, r))

    # 以下为原逻辑（去掉 input，改用上面生成的数据）
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


# 示例调用（实际使用时由外部代码调用 main(n)）
# main(5)