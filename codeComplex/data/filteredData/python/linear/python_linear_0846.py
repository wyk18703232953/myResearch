def main(n):
    if n <= 0:
        # print("NO")
        pass
        return

    # 确定性构造长度为 n 的数组：先严格递增再严格递减，保证有一个峰值
    # 示例：n=5 -> [1,2,3,2,1]
    # 对于偶数，构造一个单峰近似结构：n=4 -> [1,2,3,2]
    arr = []
    peak = n // 2
    for i in range(n):
        if i <= peak:
            arr.append(i + 1)

        else:
            arr.append(peak + 1 - (i - peak))

    x = arr.index(max(arr))
    cur = max(arr)
    l = x - 1
    r = x + 1
    ok = 1
    for _ in range(n - 1):
        if l < 0:
            ok *= (arr[r] < cur)
            cur = arr[r]
            r += 1
        elif r >= n:
            ok *= (arr[l] < cur)
            cur = arr[l]
            l -= 1

        else:
            if arr[l] > arr[r]:
                ok *= (arr[l] < cur)
                cur = arr[l]
                l -= 1

            else:
                ok *= (arr[r] < cur)
                cur = arr[r]
                r += 1
    # print("YES" if ok else "NO")
    pass
if __name__ == "__main__":
    main(10)