import random

def main(n: int) -> int:
    # 生成测试数据：整数数组 a，元素范围可根据需要调整
    # 这里生成 0 ~ n 的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    s = 0
    count = dict()
    for x in a:
        count[x] = count.get(x, 0) + 1
        s += x

    answer = 0
    for i in range(n):
        trash = 0
        trash += count.get(a[i] - 1, 0) * (a[i] - 1)
        trash += count.get(a[i], 0) * a[i]
        trash += count.get(a[i] + 1, 0) * (a[i] + 1)

        xcount = n - i
        xcount -= count.get(a[i] - 1, 0)
        xcount -= count.get(a[i], 0)
        xcount -= count.get(a[i] + 1, 0)

        answer += (s - trash) - (xcount * a[i])

        count[a[i]] -= 1
        s -= a[i]

    print(answer)
    return answer

if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)