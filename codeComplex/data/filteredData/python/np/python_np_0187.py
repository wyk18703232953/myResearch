def gen(n):
    if n == 1:
        yield '0'
        yield '1'
    else:
        for s in gen(n - 1):
            yield s + '0'
            yield s + '1'


def main(n):
    # 映射 n 为问题规模：
    # 使用 n 作为题目中原本的 n（元素个数）
    # 其余参数和数组 C 均由 n 确定性生成
    if n <= 0:
        return 0

    # 确定性生成参数 l, r, x
    # 保证有一定区间，并随 n 线性增长
    l = n * 2
    r = n * 4
    x = max(1, n // 3)

    # 确定性生成数组 C，长度为 n
    # 元素为简单的算术序列，单调递增，便于保持原逻辑意义
    C = [i + 1 for i in range(n)]

    cnt = 0
    for pos in gen(n):
        A = []
        for i in range(n):
            if pos[i] == '1':
                A.append(C[i])
        A.sort()
        if len(A):
            if l <= sum(A) <= r and A[-1] - A[0] >= x:
                cnt += 1
    return cnt


if __name__ == "__main__":
    # 示例调用，可按需修改 n 观察规模变化
    result = main(10)
    print(result)