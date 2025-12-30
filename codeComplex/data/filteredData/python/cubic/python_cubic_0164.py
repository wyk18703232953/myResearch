import random

def merge_small(c1, c2):
    if c1[1] == 1 and c2[1] == 1:
        if c1[0] == c2[0]:
            return (c1[0] + 1, 1, c1[0] + 1)
        else:
            return (c1[0], 2, c2[0])

    elif c1[1] == 2 and c2[1] == 1:
        if c1[2] == c2[0]:
            if c1[0] == c1[2] + 1:
                return (c1[0] + 1, 1, c1[0] + 1)
            else:
                return (c1[0], 2, c2[2] + 1)
        else:
            return (c1[0], 3, c2[2])

    elif c1[1] == 1 and c2[1] == 2:
        if c1[2] == c2[0]:
            if c2[2] == c2[0] + 1:
                return (c2[2] + 1, 1, c2[2] + 1)
            else:
                return (c2[0] + 1, 2, c2[2])
        else:
            return (c1[0], 3, c2[2])

    elif c1[1] == 2 and c2[1] == 2:
        if c1[2] == c2[0]:
            c1 = (c1[0], 2, c1[2] + 1)
            c2 = (c2[2], 1, c2[2])
            if c1[1] == 2 and c2[1] == 1:
                if c1[2] == c2[0]:
                    if c1[0] == c1[2] + 1:
                        return (c1[0] + 1, 1, c1[0] + 1)
                    else:
                        return (c1[0], 2, c2[2] + 1)
                else:
                    return (c1[0], 3, c2[2])
        else:
            return (c1[0], 4, c2[2])


def merge_main(c1, c2):
    if c1[1] > 2:
        if c2[1] > 2:
            if c1[2] == c2[0]:
                return (c1[0], c1[1] + c2[1] - 1, c2[2])
            else:
                return (c1[0], c1[1] + c2[1], c2[2])
        else:
            if c2[1] == 1:
                if c1[2] == c2[0]:
                    return (c1[0], c1[1], c2[2] + 1)
                else:
                    return (c1[0], c1[1] + 1, c2[2])
            if c2[1] == 2:
                if c1[2] == c2[0]:
                    if c1[2] + 1 == c2[2]:
                        return (c1[0], c1[1], c2[2] + 1)
                    else:
                        return (c1[0], c1[1] + 1, c2[2])
                else:
                    return (c1[0], c1[1] + 2, c2[2])
    else:
        if c2[1] > 2:
            if c1[1] == 1:
                if c1[2] == c2[0]:
                    return (c1[2] + 1, c2[1], c2[2])
                else:
                    return (c1[2], c2[1] + 1, c2[2])

            if c1[1] == 2:
                if c1[2] == c2[0]:
                    if c1[0] == c1[2] + 1:
                        return (c1[0] + 1, c2[1], c2[2])
                    else:
                        return (c1[0], c2[1] + 1, c2[2])
                else:
                    return (c1[0], c2[1] + 2, c2[2])
        else:
            return merge_small(c1, c2)


def main(n):
    # 根据 n 生成测试数据：这里生成 1..n 的随机排列
    if n <= 0:
        return 0
    arr = [random.randint(1, n) for _ in range(n)]

    dp_arr = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp_arr[i][i] = (arr[i], 1, arr[i])

    for length in range(1, n):            # 子区间长度差
        for l in range(n - length):       # 左端点
            r = l + length
            for k in range(l, r):         # 分割点
                res = merge_main(dp_arr[l][k], dp_arr[k + 1][r])
                if dp_arr[l][r] is None or dp_arr[l][r][1] > res[1]:
                    dp_arr[l][r] = res

    # 输出与原程序一致的结果：dp_arr[0][n-1][1]
    print(dp_arr[0][n - 1][1])
    return dp_arr[0][n - 1][1]


if __name__ == "__main__":
    # 示例：运行规模 n = 5
    main(5)