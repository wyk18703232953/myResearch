import random

def gen(n):
    if n == 1:
        yield '0'
        yield '1'
    else:
        for s in gen(n - 1):
            yield s + '0'
            yield s + '1'


def main(n):
    # 根据规模 n 生成测试数据
    # 生成 n 个难度值 C[i]，范围可自行调整，这里设为 1~100
    C = [random.randint(1, 100) for _ in range(n)]
    C.sort()

    # 为了产生有意义的约束，构造 l, r, x
    total_sum = sum(C)
    min_c, max_c = C[0], C[-1]

    # 随机生成一个子区间 [l, r]，覆盖总和的一部分
    l = random.randint(0, total_sum // 2)
    r = random.randint(total_sum // 2, total_sum)

    # x 取一个不超过最大差值的随机值
    x = random.randint(0, max_c - min_c if max_c > min_c else 0)

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

    # 输出结果（也可以改为 return cnt, C, l, r, x 供外部使用）
    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)