def solution(n, k):
    ret = [['.' for _ in range(n)] for _ in range(4)]
    if 1 == k & 1:
        ret[1][n >> 1] = '#'
        for i in range(1, n >> 1):
            if k < 2:
                break
            k -= 2
            ret[1][i] = '#'
            ret[1][n - 1 - i] = '#'
        for i in range(1, n >> 1):
            if k < 2:
                break
            k -= 2
            ret[2][i] = '#'
            ret[2][n - 1 - i] = '#'
    else:
        for i in range(1, n - 1):
            if k < 2:
                break
            k -= 2
            ret[1][i] = '#'
            ret[2][i] = '#'

    print('YES')
    for i in range(4):
        print(''.join(ret[i]))


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 k，使得不会超过能填充的最大数量
    # 最大可填 '#': 2 * (n - 2)
    max_k = 2 * (n - 2)
    if max_k < 1:
        k = 0
    else:
        # 示例：取一个中等规模的 k
        k = max_k // 2
        # 保留原逻辑中对奇偶的分支效果，可以自由改为奇数或偶数
        if k % 2 == 0:
            k += 1
            if k > max_k:
                k -= 2  # 退回到合法范围内的奇数

    solution(n, k)


if __name__ == "__main__":
    # 示例调用：可按需要修改 n
    main(10)