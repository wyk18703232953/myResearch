import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1~100 之间的随机整数
    l = [random.randint(1, 100) for _ in range(n)]

    b_sum = 0
    l.sort()
    for i in l:
        b_sum += i

    m_sum = 0
    c = 0
    for i in l[::-1]:
        m_sum += i
        c += 1
        if m_sum > (b_sum / 2):
            break

    print(c)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)