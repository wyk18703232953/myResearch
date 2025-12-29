import random

def main(n):
    # 生成测试数据：a 和 b 为 1..n 的随机排列
    a = list(range(1, n + 1))
    b = a.copy()
    random.shuffle(a)
    random.shuffle(b)

    # 原逻辑开始
    a = a[::-1]
    c = [0] * n
    bk = []
    for i in range(n):
        co = 0
        if c[b[i] - 1] == 0:
            while a and a[-1] != b[i]:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
            if a:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
        bk.append(co)
    print(*bk)

# 示例调用
if __name__ == "__main__":
    main(10)