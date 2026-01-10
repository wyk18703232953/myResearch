val = 10**9

def main(n):
    # 解释输入结构：
    # 原程序输入为：
    # n m
    # n 行，每行一个整数 -> arr1
    # m 行，每行三个整数 x1 x2 y
    #
    # 在重构中，我们用 n 来同时控制：
    # - n: arr1 的长度
    # - m: 查询的数量
    #
    # 为了使规模合理，这里设定：
    # 原始 n = n
    # 原始 m = n
    #
    # 所有数据使用确定性构造。

    original_n = n
    original_m = n

    # 构造 arr1，长度为 original_n
    # 使用简单的算术构造：i * 2 + 1
    arr1 = [(i * 2 + 1) for i in range(original_n)]
    arr1.append(val)

    arr2 = []
    ans = val
    finalval = 0

    arr1.sort()

    # 构造 original_m 组 (x1, x2, y)
    # x1 在 {0,1} 中确定性变化；当 x1 == 1 时才可能影响逻辑
    # x2 用 i*3 的形式构造，并保证覆盖一部分 arr1 和 val
    # y 不参与逻辑，构造一个确定性值即可
    for i in range(original_m):
        x1 = 1 if i % 2 == 0 else 0
        x2 = (i * 3) if (i % 5 != 0) else val  # 偶尔让 x2 == val 以触发 finalval 分支
        y = i  # 占位，无实际使用

        if x1 == 1:
            if x2 == val:
                finalval += 1
            else:
                if len(arr1) > 0 and x2 >= arr1[0]:
                    arr2.append(x2)

    arr2.sort()
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] == arr2[j]:
            temp1 = len(arr2) - j
            ans = min(i + temp1, ans)
            i += 1
        else:
            temp1 = len(arr2) - j
            ans = min(i + temp1, ans)
            i += 1

    ans = min(i, ans)
    print(ans + finalval)


if __name__ == "__main__":
    main(10)