import random

def main(n):
    # 生成测试数据：长度为 n 的随机整数数组
    l = [random.randint(0, 100) for _ in range(n)]

    m = l[:]
    m.sort()
    f = 1
    c = 0
    for i in range(n):
        if l[i] != m[i]:
            c += 1
        if c > 2:
            f = 0
            break
    if f == 0:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)