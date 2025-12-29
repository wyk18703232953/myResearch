import random

MOD = int(1e9 + 7)


def prefix_sums(A):
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for k in range(1, n):
        P[k] = int((P[k - 1] + A[k]) % MOD)
    return P


def main(n: int) -> int:
    # 生成测试数据：长度为 n 的指令串，仅由 'f' 和 's' 组成
    # 保持与原程序一致的语义：s 是将多行输入串接后的结果
    s = "".join(random.choice(["f", "s"]) for _ in range(n))

    arr = [[0] * n for _ in range(n)]

    def find_ans():
        idx = 0  # 保留原变量，虽然逻辑中未使用其值
        for i in range(len(arr) - 1):
            arr[0][0] = 1

            if s[i] == 'f':
                for j in range(0, len(arr)):
                    arr[i + 1][0] = 0
                    if j > 0:
                        arr[i + 1][j] = arr[i][j - 1]
                        idx = i + 1
            else:
                arr[i + 1] = prefix_sums(arr[i][::-1])[::-1]
        return arr

    if n == 1 or 'f' not in s:
        if s[0] == 's':
            return 1
        else:
            return int(sum(find_ans()[-1]) % MOD)
    else:
        return int(sum(find_ans()[-1]) % MOD)


if __name__ == "__main__":
    # 示例：调用 main(5) 运行一次
    print(main(5))