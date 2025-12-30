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
    # 生成测试数据：
    # n: 数组长度
    # q: 查询次数，这里设为 n，当然可根据需要调整
    q = n

    # 生成 arr：正整数，保证递增前缀和有意义
    # 为避免数值过大，每个元素在 1~10 之间
    arr = [random.randint(1, 10) for _ in range(n)]

    # 生成 brr：正整数查询
    brr = [random.randint(1, 10) for _ in range(q)]

    # 以下逻辑与原 main 完全一致
    su = sum(arr)
    curr = 0
    for i in range(1, n):
        arr[i] = arr[i] + arr[i - 1]

    for b in brr:
        curr += b
        pos = n - bin_ser(arr, curr) - 1
        if pos == 0:
            pos = n
        print(pos)
        if curr >= su:
            curr = 0


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)