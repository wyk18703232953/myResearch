import random

def main(n: int):
    # 生成测试数据：n个互不相等的随机整数
    # 为了更清晰地测试，可让数组形成一个“山峰”结构
    # 示例策略：随机生成 n 个整数再打乱
    arr = list(range(1, n + 1))
    random.shuffle(arr)

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
    print("YES" if ok else "NO")


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)