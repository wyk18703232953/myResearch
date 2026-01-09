def main(n):
    # n 表示两个数组的长度
    if n <= 0:
        return

    # 确定性生成测试数据
    # arr1: 0, 1, 2, ..., n-1
    # arr2: 0, 2, 4, ..., 2*(n-1)
    arr1 = [i for i in range(n)]
    arr2 = [2 * i for i in range(n)]

    # 原核心逻辑：暴力双重循环找交集并输出
    output = []
    for first in arr1:
        for second in arr2:
            if first == second:
                output.append(str(first))
                break  # 原算法一旦找到相等即可，不再多余比较同一 first

    if output:
        # print(" ".join(output))
        pass
if __name__ == "__main__":
    main(10)