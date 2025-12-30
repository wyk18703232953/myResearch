import random

def main(n):
    # 根据规模 n 生成测试数据（这里随机生成 [0, n] 范围内的整数）
    a = [random.randint(0, n) for _ in range(n)]

    c = 0
    for i in range(n):
        if a[i] > c:
            print(i + 1)
            break
        else:
            c = max(a[i] + 1, c)
    else:
        print(-1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)