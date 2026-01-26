def replace(arr):
    if arr == [1] * len(arr):
        arr[-1] = 2
        # print(*sorted(arr))
        pass
        return ""
    arr[arr.index(max(arr))] = 1
    # print(*sorted(arr))
    pass
    return ""

def main(n):
    # 规模 n 表示列表长度
    if n <= 0:
        return ""
    # 确定性构造：前半部分为 1，后半部分为递增整数
    half = n // 2
    lst = [1] * half + [i + 2 for i in range(n - half)]
    return replace(lst)

if __name__ == "__main__":
    main(10)