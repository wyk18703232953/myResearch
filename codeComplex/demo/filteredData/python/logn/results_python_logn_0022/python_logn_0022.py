def main(n):
    # 生成确定性输入：让 a 和 b 与 n 线性相关
    # 保证 a <= b 且二者不同，以触发核心逻辑
    a = n
    b = 2 * n + 1

    a, b = min(a, b), max(a, b)
    A = bin(a)[2:]
    B = bin(b)[2:]
    A = "0" * (len(B) - len(A)) + A
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff = len(A) - i
            break
    result = (2 ** diff) - 1
    return result


if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass