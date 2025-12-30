import random

def main(n):
    # 生成测试数据：1~n 的随机排列（保证 a[j]-1 始终在 [0, n-1] 范围内）
    a = list(range(1, n + 1))
    random.shuffle(a)

    arr = a[:]  # 复制一份，保留原始测试数据如需调试可用
    n = len(arr)
    u = n
    for i in range(n):
        j = i
        k = 0
        while arr[j] > 0:
            k += 1
            t = j
            j = arr[j] - 1
            arr[t] = 0
        if k > 0:
            u += 1 - k % 2
    s = 'Petr'
    if u % 2 > 0:
        s = 'Um_nik'
    print(s)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)