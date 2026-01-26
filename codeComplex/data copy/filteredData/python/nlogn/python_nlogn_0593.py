def solve(N, M, A):
    A.sort(reverse=True)

    lh = A[0]
    cnt = 1
    for a in A[1:]:
        if lh == 1:
            cnt += 1
        elif lh - 1 <= a:
            cnt += 1
            lh -= 1

        else:
            cnt += lh - a
            lh = a

    cnt += lh - 1

    return sum(A) - cnt


def main(n):
    # n 作为 N 的规模，M 按与 N 同规模生成
    N = n if n > 0 else 1
    M = n if n > 0 else 1

    # 生成确定性的数组 A，长度为 N，元素依赖 i 的简单算术
    # 保证所有元素为正整数
    A = [(i % (M + 1)) + 1 for i in range(N)]

    result = solve(N, M, A)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以改变规模
    main(10)