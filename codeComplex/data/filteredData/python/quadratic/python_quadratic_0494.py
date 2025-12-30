import random

def main(n):
    # 生成一个“有解”的测试数据 (a,b)，然后再跑原逻辑进行校验
    #
    # 思路：
    # 1. 随机生成一个排列 zz[0..n-1]，其中元素是 1..n 的一个排列；
    # 2. 根据 zz 计算：
    #       a[i] = 左侧比 zz[i] 大的数的数量
    #       b[i] = 右侧比 zz[i] 大的数的数量
    # 3. 然后用题目给的逻辑检查 (a,b)，并输出结果。
    #
    # 这样就避免了直接构造 (a,b) 的困难，同时保证大部分情况下是 YES。
    if n <= 0:
        return

    # 1. 随机生成 zz 为 1..n 的一个排列
    zz = list(range(1, n + 1))
    random.shuffle(zz)

    # 2. 根据 zz 计算 a、b
    a = [0] * n
    b = [0] * n
    for i in range(n):
        # 左边比 zz[i] 大的数量
        cnt_left = 0
        for j in range(i):
            if zz[j] > zz[i]:
                cnt_left += 1
        a[i] = cnt_left

        # 右边比 zz[i] 大的数量
        cnt_right = 0
        for j in range(i + 1, n):
            if zz[j] > zz[i]:
                cnt_right += 1
        b[i] = cnt_right

    # 3. 使用给定的逻辑，对生成的 a,b 进行同样的处理和输出
    fl = True

    # 先做边界检查
    for i in range(n):
        if a[i] > i:
            fl = False
        if b[i] > (n - i - 1):
            fl = False
        if (n - a[i] - b[i]) <= 0:
            fl = False

    if not fl:
        print("NO")
        return

    # 计算根据公式还原出的 zz2，并再验证一次
    zz2 = [0] * n
    for i in range(n):
        zz2[i] = (n - a[i] - b[i])

    for i in range(n):
        xl = 0
        xr = 0
        for j in range(i + 1, n):
            if zz2[j] > zz2[i]:
                xr += 1
        for j in range(i - 1, -1, -1):
            if zz2[j] > zz2[i]:
                xl += 1
        if xl != a[i] or xr != b[i]:
            fl = False
            break

    if fl:
        print("YES")
        print(*zz2)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(5)