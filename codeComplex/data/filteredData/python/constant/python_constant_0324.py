import random

def main(n):
    # 生成规模为 n 的测试数据，这里使用 0~100 的随机整数
    v = [random.randint(0, 100) for _ in range(n)]
    # 也可以根据需要改成特定数据，例如：
    # v = list(range(1, n + 1))

    val = 0
    for i in range(n):
        a = v[i] // n
        arr = v.copy()
        arr[i] = 0
        for j in range(n):
            arr[j] += a
        b = v[i] % n
        k = i + 1
        l = 0
        while l < b:
            if k > n - 1:
                k = 0
            arr[k] += 1
            k += 1
            l += 1

        count = 0
        for j in range(n):
            if arr[j] % 2 == 0:
                count += arr[j]
        val = max(val, count)
    print(val)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)