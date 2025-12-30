import random

def main(n):
    # 根据 n 生成测试数据
    # 这里假设 m 取一个 1~n 的中间值，例如 n//2（至少为 1）
    m = max(1, n // 2)
    # 生成长度为 n 的整数列表，这里取值范围 -10^4 ~ 10^4 可自行调整
    lst = [random.randint(-10000, 10000) for _ in range(n)]

    maxx = 0.0
    arr = [0.0] * (n + 1)

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += lst[j]
            length = j - i + 1
            avg = summ / length
            if avg > arr[length - 1]:
                arr[length - 1] = avg

    print(max(arr[m - 1:]))

if __name__ == "__main__":
    # 示例：调用 main，n 可按需要修改
    main(10)