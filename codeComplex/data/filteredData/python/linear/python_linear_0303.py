from math import ceil

def main(n):
    # 根据 n 生成测试数据，这里生成一个简单的递增序列作为示例
    # 可按需要修改数据生成逻辑
    a = [i for i in range(n)]

    p = 0
    ans = float('inf')
    for i in range(n):
        turns = ceil((a[i] - i) / n)
        if turns < ans:
            ans = turns
            p = i
    print(p + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)