import random

def main(n):
    # 根据规模 n 生成测试数据
    # 示例规则：a, b, c, n 都在 [0, n] 范围内
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, n)
    total_n = random.randint(0, n)

    u = a + b - c
    if a < c or b < c:
        print(-1)
    else:
        if total_n - u >= 1:
            print(total_n - u)
        else:
            print(-1)

if __name__ == "__main__":
    # 示例：调用 main(100) 进行一次测试
    main(100)