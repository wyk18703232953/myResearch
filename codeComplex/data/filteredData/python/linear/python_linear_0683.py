import random

def main(n):
    # 生成测试数据 b，长度为 n//2，b[0] 特殊处理保证非负
    half = n // 2
    if half == 0:
        print()
        return

    # 先构造一个可行的 a，然后按原逻辑反推 b
    # 构造 a：让它在 [0, 10] 范围内随机
    a = [0] * n
    for i in range(half):
        a[i] = random.randint(0, 10)
        a[n - 1 - i] = random.randint(0, 10)

    b = [0] * half
    # 按原题思路构造 b，其中 b[i] = a[i] + a[n-1-i] 的某种约束形式
    # 这里简单使用 b[i] = a[i] + a[n-1-i]
    for i in range(half):
        b[i] = a[i] + a[n - 1 - i]

    # 使用题目提供的算法逻辑（只是不再从 input 读入）
    # 下面重新从 b 推回一个 a_ans，验证算法逻辑
    a_ans = [0] * n

    minV = 0
    maxV = b[0]

    m = n // 2

    a_ans[n - 1] = b[0]

    i = 1
    j = n - 2

    while i < m:
        if (b[i] - minV > 0 and b[i] - minV <= maxV):
            a_ans[i] = minV
            a_ans[j] = b[i] - minV
            maxV = min(maxV, b[i] - minV)
        else:
            a_ans[i] = b[i] - maxV
            a_ans[j] = maxV
            minV = max(minV, b[i] - maxV)

        i += 1
        j -= 1

    print(' '.join(map(str, a_ans)))


if __name__ == "__main__":
    # 示例：调用 main(6)
    main(6)