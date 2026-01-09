def main(n):
    # 构造确定性数组 arr，长度为 n
    # 规则：前半部分非递减，后半部分非增，且保证元素 n 一定在数组中
    if n <= 0:
        return

    arr = [0] * n
    mid = n // 2

    # 前半部分：非递减序列
    for i in range(mid):
        arr[i] = i

    # 把 n 放在位置 mid（若可行），若 mid 越界则放在最后一个位置
    idx = mid if mid < n else n - 1
    arr[idx] = n

    # 后半部分：非增序列，从 n 开始往下
    val = n
    for i in range(idx + 1, n):
        val -= 1
        arr[i] = val

    # 保持原程序逻辑
    idx_in_arr = arr.index(n)
    ok = 1
    for i in range(1, idx_in_arr):
        if arr[i] < arr[i - 1]:
            ok = 0
    for i in reversed(range(idx_in_arr, n - 1)):
        if arr[i] < arr[i + 1]:
            ok = 0
    if ok:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)