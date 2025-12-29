import random

def main(n: int):
    # 1. 生成测试数据：n 个正整数
    # 可根据需要修改数据范围
    l = [random.randint(1, 100) for _ in range(n)]

    # 2. 按原逻辑处理
    l = sorted(l)
    s = 0
    c = 0
    cnt = 0

    for i in l:
        s += i

    for i in l[::-1]:
        c += i
        cnt += 1
        if c > (s / 2):
            break

    # 3. 输出结果
    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main，n 为数据规模
    main(10)