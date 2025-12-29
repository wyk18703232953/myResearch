import random

def main(n: int):
    # 生成测试数据：长度为 n 的随机整数数组
    # 这里假设元素为 1~10^9 之间的随机数，可按需要调整
    arr = [random.randint(1, 10**9) for _ in range(n)]

    ans = 10 ** 10
    for i in range(n):
        x = i if i > n - i - 1 else n - i - 1
        # 避免除以 0，当 x 为 0 时跳过（原逻辑会出现 i=0 或 i=n-1）
        if x == 0:
            continue
        ans = min(ans, arr[i] // x)

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)