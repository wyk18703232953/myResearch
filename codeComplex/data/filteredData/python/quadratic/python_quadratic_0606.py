import random

def main(n):
    # 根据 n 生成测试数据
    # 这里约定：
    #   m 在 [1, n] 随机
    #   k 在 [-10, 10] 随机
    #   数组 aa 的元素在 [-10, 10] 随机
    if n <= 0:
        return 0

    m = random.randint(1, n)
    k = random.randint(-10, 10)
    aa = [random.randint(-10, 10) for _ in range(n)]

    ans = 0
    for start in range(m):
        ac = aa[:]  # 拷贝数组
        for i in range(start, n, m):
            ac[i] -= k
        cur = 0
        for i in range(start, n):
            if i % m == start:
                cur = max(ac[i] + cur, ac[i])
            else:
                cur += ac[i]
            ans = max(cur, ans)
    print(ans)
    return ans

if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)