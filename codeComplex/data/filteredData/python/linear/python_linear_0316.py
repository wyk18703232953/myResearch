from random import randint

def main(n):
    # 生成测试数据：
    # 原程序读取 n, m 和长度为 n 的数组 arr
    # 这里：
    #   m 取一个与 n 有关的正整数（至少为 1）
    #   arr 生成为 [0, 1e9] 范围内的随机整数
    if n <= 0:
        return

    # 生成参数
    m = max(1, n // 2)  # 例如：取 m = n//2，至少为 1
    arr = [randint(0, 10**9) for _ in range(n)]

    # 原逻辑开始
    s = sum(arr)
    idx = [[] for _ in range(m)]
    for i in range(n):
        idx[arr[i] % m].append(i)

    j = 0
    target = n // m  # 每个余数类的目标元素个数
    for i in range(m):
        while len(idx[i]) > target:
            while j < i or len(idx[j % m]) >= target:
                j += 1
            last = idx[i].pop()
            arr[last] += (j - i) % m
            idx[j % m].append(last)

    # 输出结果
    print(sum(arr) - s)
    print(*arr)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)