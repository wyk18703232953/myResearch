import random

def main(n):
    # 生成规模为 n 的测试数据：随机整数序列（范围可自行调整）
    s = [str(random.randint(0, 100)) for _ in range(n)]

    l = []
    for j in s:
        v = int(j) % 2
        if not l or v != l[-1]:
            l.append(v)
        else:
            l.pop()

    if len(l) < 2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main，n 可自行修改
    main(10)