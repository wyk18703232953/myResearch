import random

def main(n):
    # 生成测试数据：n 和 k 以及长度为 n 的数组 l
    # 这里示例生成：
    #   1) k 在 [1, n] 内随机
    #   2) l 是 n 个 [-100, 100] 之间的随机整数
    if n <= 0:
        return

    k = random.randint(1, n)
    l = [random.randint(-100, 100) for _ in range(n)]

    ans = float('-inf')
    for i in range(n):
        avg, count = 0, 0
        for j in range(i, n):
            count += l[j]
            if j - i + 1 >= k:
                avg = count / (j - i + 1)
                if avg > ans:
                    ans = avg

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)