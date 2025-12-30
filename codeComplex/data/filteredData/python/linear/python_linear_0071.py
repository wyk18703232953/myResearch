import random

def main(n: int):
    # 生成测试数据
    # s 设为一个与 n 同量级的正整数
    s = random.randint(1, 10 * n if n > 0 else 10)

    arr = []
    for _ in range(n):
        # arr[i][0]、arr[i][1] 生成非负整数（可按需要调整范围）
        a0 = random.randint(0, 10 * n if n > 0 else 10)
        a1 = random.randint(0, 10 * n if n > 0 else 10)
        arr.append([a0, a1])

    # 以下为原逻辑
    arr = sorted(arr, reverse=True, key=lambda x: x[0])
    ans, c = 0, 0
    for i in range(n):
        if i != 0:
            c = arr[i - 1][0]
        if i == 0:
            ans = ans + s - arr[i][0]
        else:
            ans = ans + c - arr[i][0]
        if arr[i][1] >= ans:
            ans = ans + (arr[i][1] - ans)
    if n > 0:
        ans = ans + arr[n - 1][0]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)