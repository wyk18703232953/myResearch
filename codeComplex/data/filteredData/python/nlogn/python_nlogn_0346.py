import random

def main(n: int):
    # 生成规模为 n 的测试数据（整数数组）
    # 这里生成 [-10^9, 10^9] 区间内的随机整数
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    arr.sort()
    s = set(arr)
    flag = False
    ans = []

    # 尝试找到长度为 3 的等差序列，公差为 2 的幂
    for ele in arr:
        for i in range(31):
            d = 1 << i
            if (ele - d) in s and (ele + d) in s:
                ans = [ele, ele - d, ele + d]
                flag = True
                break
        if flag:
            break

    if flag:
        print(3)
        print(*ans)
        return

    # 尝试找到长度为 2 的等差序列，公差为 2 的幂
    for ele in arr:
        for i in range(31):
            d = 1 << i
            if (ele + d) in s:
                ans = [ele, ele + d]
                flag = True
                break
        if flag:
            break

    if flag:
        print(2)
        print(*ans)
    else:
        print(1)
        print(arr[0])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)