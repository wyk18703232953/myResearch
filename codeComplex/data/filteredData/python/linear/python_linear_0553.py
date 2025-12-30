import random

def main(n):
    # 生成规模为 n 的测试数据
    # 这里示例为：在 [0, n] 范围内随机生成 n 个整数
    a = [random.randint(0, n) for _ in range(n)]

    s = 0
    for j, i in enumerate(a):
        if i > s:
            print(j + 1)
            return
        if i == s:
            s += 1
    print(-1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)