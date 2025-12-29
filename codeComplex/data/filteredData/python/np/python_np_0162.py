import random

def main(n):
    # 生成测试数据
    # n: 题目规模（元素个数）
    # l, r: 选取子集和的区间
    # x: 最大值与最小值之差的下限

    # 生成难度数组 a，范围自定
    a = [random.randint(1, 100) for _ in range(n)]
    a.sort()  # 排序不影响原逻辑，但更接近常见出题习惯

    # 生成 l, r, x
    total_sum = sum(a)
    # 为了保证存在解的可能性，大致设定范围
    l = random.randint(0, max(0, total_sum // 4))
    r = random.randint(max(l, total_sum // 4), total_sum)
    x = random.randint(0, max(a) - min(a) if n >= 2 else 0)

    ans = 0
    # 1 到 (2^n - 1)，原代码用了 (2**n)+1，且从1开始，到2**n包括
    for i in range(1, (1 << n) + 1):
        j = bin(i)[2:]
        if len(j) < n:
            j = '0' * (n - len(j)) + j

        c = 0
        temp = []
        for k in j:
            if k == '1':
                temp.append(a[c])
            c += 1

        s = sum(temp)
        if len(temp) >= 2 and l <= s <= r and (max(temp) - min(temp)) >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)