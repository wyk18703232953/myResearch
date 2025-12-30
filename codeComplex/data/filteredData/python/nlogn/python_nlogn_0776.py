import random

def main(n):
    # 生成规模为 n 的测试数据：n 个在 1~10^9 之间的随机整数
    li = [random.randint(1, 10**9) for _ in range(n)]

    x = li.index(max(li))
    if li[:x] == sorted(li[:x]) and li[x:] == sorted(li[x:])[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可自行修改 n 测试不同规模
    main(10)