def check(temp, l, r, x):
    if len(temp) < 2:
        return False
    s = sum(temp)
    if l <= s <= r:
        if temp[-1] - temp[0] >= x:
            return True
        else:
            return False
    else:
        return False


def brute(index, temp, arr, n, l, r, x, count_holder):
    if index == n:
        if check(temp, l, r, x):
            count_holder[0] += 1
    else:
        temp.append(arr[index])
        brute(index + 1, temp, arr, n, l, r, x, count_holder)
        temp.pop()
        brute(index + 1, temp, arr, n, l, r, x, count_holder)


def main(n):
    # n 表示题目中原本的 n：元素个数
    # 构造与示例结构类似但可规模化、确定性的输入
    # 约束区间随 n 缩放，以保证有一定数量的合法子集
    l = n * 2
    r = n * 4
    x = max(1, n // 5)
    arr = [i + 1 for i in range(n)]
    arr.sort()
    count_holder = [0]
    brute(0, [], arr, n, l, r, x, count_holder)
    print(count_holder[0])


if __name__ == "__main__":
    main(10)