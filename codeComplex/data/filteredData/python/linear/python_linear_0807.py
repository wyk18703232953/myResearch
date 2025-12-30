import random

def main(n):
    # 生成测试数据
    # 规模 n 控制原数组长度；m,k 也一起按 n 规模生成
    m = n
    k = max(1, n // 5)  # 确保 k >= 1
    # 生成升序且 >0 的数组元素，模拟原题常见数据形态
    arr = []
    cur = 1
    for _ in range(n):
        cur += random.randint(0, 2)
        arr.append(cur)

    # 原逻辑开始
    arr = arr[:]  # 确保不修改原列表引用
    arr += [0] * m
    ans = 0
    pos = 0
    while arr[pos] != 0:
        page = (arr[pos] - pos - 1) // k
        tmp = 1
        for i in range(1, k):
            if pos + i >= 2 * m - 1:
                break
            if (arr[pos + i] - pos - 1) // k == page:
                tmp += 1
            else:
                break
        pos += tmp
        ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例运行
    main(10)