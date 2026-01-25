from math import ceil

def main(n):
    # 生成确定性输入：n 和数组 a
    # 映射：输入规模 n -> 数组长度为 n
    # 构造 a 为一个确定性整数序列，保证 a[i] >= i，以避免负轮次
    a = [i + 2 for i in range(n)]

    p = 0
    ans = float('inf')
    for i in range(n):
        turns = ceil((a[i] - i) / n)
        if turns < ans:
            ans = turns
            p = i
    print(p + 1)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小做复杂度实验
    main(10)