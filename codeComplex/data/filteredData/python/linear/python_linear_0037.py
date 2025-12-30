import random

def find_segment(arr, n, k):
    f = [0] * 100001
    L = 0
    count = 0
    R = -1
    while R < n - 1:
        R += 1
        if f[arr[R]] == 0:
            count += 1
        f[arr[R]] += 1
        while count == k:
            f[arr[L]] -= 1
            if f[arr[L]] == 0:
                print(L + 1, R + 1)
                return
            L += 1
    print(-1, -1)

def main(n):
    # 生成测试数据：
    # n：数组长度
    # k：目标不同元素个数，设为 1 到 min(n, 50) 之间的随机值
    k = random.randint(1, min(n, 50))
    # 元素值范围控制在 [1, 10^5] 以内，与原代码频次数组兼容
    max_val = 100000
    arr = [random.randint(1, max_val) for _ in range(n)]

    # 输出生成的数据（如果不需要，可以删除这两行打印）
    print("n =", n, "k =", k)
    print("arr =", arr)

    find_segment(arr, n, k)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在此修改 n 的值
    main(10)