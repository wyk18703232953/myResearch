def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 使用简单的算术构造，保证可重复
    arr = [(i * 7 + 3) % (n + 5) for i in range(n)] if n > 0 else []

    if n == 0:
        # print("NO")
        pass
        return

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