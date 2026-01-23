def comp(arr):    
    for i in range(len(arr)-1):    
        for j in range(0, len(arr)-i-1):
            if arr[j] in arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[::-1]


def main(n):
    # n 表示字符串数量
    if n <= 0:
        return

    # 构造确定性的字符串数组
    # 第 j 个字符串是从 'a' 开始长度为 j+1 的前缀
    # 这样保证后一个字符串总是包含前一个
    base = "abcdefghijklmnopqrstuvwxyz"
    arr = []
    for j in range(1, n + 1):
        # 为了可扩展，当 j 超过 26 时，多重复几轮字母表
        times = (j + len(base) - 1) // len(base)
        s = (base * times)[:j]
        arr.append(s)

    t = n
    ans = 1

    arr = comp(arr)

    for j in range(0, t - 1):
        if arr[j] not in arr[j + 1]:
            ans = 0
            break

    if ans == 0:
        print("NO")
    else:
        print("YES")
        for j in arr:
            print(j)


if __name__ == "__main__":
    main(5)