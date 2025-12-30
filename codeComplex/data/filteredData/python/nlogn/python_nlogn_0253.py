import random

def bin_ser(arr, curr):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= curr:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


def main(n):
    # 生成测试数据
    # arr 为长度为 n 的正整数数组
    # brr 长度也取为 n
    random.seed(0)
    arr = [random.randint(1, 10) for _ in range(n)]
    brr = [random.randint(1, 10) for _ in range(n)]

    su = sum(arr)
    curr = 0

    # 前缀和
    for i in range(1, n):
        arr[i] = arr[i] + arr[i - 1]

    # 模拟原逻辑输出
    for b in brr:
        curr += b
        pos = n - bin_ser(arr, curr) - 1
        if pos == 0:
            pos = n
        print(pos)
        if curr >= su:
            curr = 0


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)