def main(n):
    # 映射含义：
    # n -> 原程序中的 n（数组长度）
    # m 仍保留为一个参数，但原代码未使用 m 的值，只是从输入中读取
    # 这里令 m = n，保证结构一致但不影响逻辑
    if n <= 0:
        return

    m = n

    # 构造确定性的数组 A，长度为 n
    # 原代码对 A 只做排序和数值比较，这里用一个简单的算术序列
    # 为了让逻辑更丰富一些，引入重复和不同大小的值
    A = [(i * 3) // 2 % (n // 2 + 1) + 1 for i in range(n)]

    if n == 1:
        print(0)
        return

    A.sort(reverse=True)

    NOW = A[0]
    ANS = 1
    i = 1
    while i < n:
        if A[i] == A[i - 1]:
            NOW = max(1, NOW - 1)
            ANS += 1
        else:
            if A[i] >= NOW - 1:
                ANS += 1
                NOW = max(NOW - 1, 1)
            else:
                ANS += max(1, NOW - A[i])
                NOW = A[i]
        i += 1

    ANS += (NOW - 1)
    print(sum(A) - ANS)


if __name__ == "__main__":
    main(10)