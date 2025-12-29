def main(n):
    # n 作为查询的 k 值规模，示例：对 k = 1..n 依次执行原逻辑
    A = [9, 189, 2889, 38889, 488889, 5888889, 68888889,
         788888889, 8888888889, 98888888889, 1088888888889]

    # 为避免 A[n+1] 越界，最多到 len(A)-2
    max_block_index = len(A) - 2

    for k in range(1, n + 1):
        if k < 10:
            print(k)
        else:
            for idx in range(0, max_block_index + 1):
                if k > A[idx + 1]:
                    continue
                a = 10 ** (idx + 1) + (k - A[idx] - 1) // (idx + 2)
                b = (k - A[idx] - 1) % (idx + 2)
                print(str(a)[b])
                break


if __name__ == "__main__":
    # 示例：规模 n = 50
    main(50)