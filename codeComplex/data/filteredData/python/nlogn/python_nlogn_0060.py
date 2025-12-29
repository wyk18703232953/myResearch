import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机整数列表 a
    # 可根据需要调整数值范围
    a = [random.randint(1, 100) for _ in range(n)]

    # 原代码逻辑开始
    k = sorted(a)
    b = 0
    q = 0
    m = 0

    for i in k:
        b = b + i
    for i in k[::-1]:
        q = q + i
        m = m + 1
        if q > (b / 2):
            break

    print(m)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)