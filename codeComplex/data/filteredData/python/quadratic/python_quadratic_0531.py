import random

def main(n: int):
    # 生成测试数据：a 和 b 都是 1..n 的随机排列
    a = list(range(1, n + 1))
    b = list(range(1, n + 1))
    random.shuffle(a)
    random.shuffle(b)

    # 将原始代码逻辑搬入此处
    a = a[::-1]  # 原代码中立刻对 a 反转
    ans = [0] * n
    marked = [True] * (n + 1)

    for i in range(n):
        if marked[b[i]]:
            while True:
                marked[a[-1]] = False
                ans[i] += 1
                if a[-1] == b[i]:
                    a.pop()
                    break
                a.pop()
        else:
            continue

    print(*ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 的大小进行测试
    main(5)