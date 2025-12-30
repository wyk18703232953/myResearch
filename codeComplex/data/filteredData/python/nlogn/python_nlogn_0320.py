import random

def main(n: int):
    # 生成测试数据：随机生成 0..n-1 的一个排列作为 a
    # 原代码中 a 是 1-based，下标 i 的值 a[i] 是一个“指向”下标的映射
    # 这里生成 0..n-1 的随机排列，再整体 +1，使其变成 1..n 的排列
    perm = list(range(1, n + 1))
    random.shuffle(perm)

    # 构造与原代码一致的数组 a：[0] 占位，1..n 为实际数据
    a = [0] + perm

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

    if n % 2 == 0:
        # n even ans also even even number of swaps required
        # 3*n 
        if ans % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")
    else:
        # n us odd ans is even odd number of swaps required
        if ans % 2 == 0:
            print("Petr")
        else:
            print("Um_nik")


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)