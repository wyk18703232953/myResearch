import random

def main(n):
    # 根据 n 生成测试数据：生成一个长度为 n 的随机整数数组
    # 这里生成范围在 1 到 10^9 之间的随机整数
    arr = [random.randint(1, 10**9) for _ in range(n)]

    ab = sorted(arr)
    t = [i for i in range(n) if arr[i] != ab[i]]
    if len(t) < 3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)