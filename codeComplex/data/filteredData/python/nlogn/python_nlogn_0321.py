import random

def main(n: int):
    # 生成测试数据：1..n 的一个随机排列
    perm = list(range(1, n + 1))
    random.shuffle(perm)

    # 原代码逻辑开始
    a = [0] + perm[:]  # 保持与原程序相同的下标习惯（1 到 n）
    ans = 0
    for i in range(1, len(a)):
        if a[i] == -1:
            continue
        j = i
        while a[j] != -1:
            prev = j
            j = a[j]
            a[prev] = -1
        ans += 1

    # 判断并输出
    if n % 2 == 0:
        # n even ans also even even number of swaps required
        # 3*n
        if ans % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")
    else:
        # n is odd ans is even odd number of swaps required
        if ans % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)