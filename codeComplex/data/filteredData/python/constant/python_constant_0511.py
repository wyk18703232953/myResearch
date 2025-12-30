import random

def main(n):
    # 生成 n 组测试数据 (x, y, k)，这里可按需要调整范围
    test_cases = []
    for _ in range(n):
        x = random.randint(0, 10**6)
        y = random.randint(0, 10**6)
        k = random.randint(0, 10**6)
        test_cases.append((x, y, k))

    # 按原逻辑处理并输出结果
    for x, y, k in test_cases:
        if max(x, y) > k:
            print(-1)
        else:
            if (x + y) % 2 == 0:
                if k % 2 == max(x, y) % 2:
                    print(k)
                else:
                    print(k - 2)
            else:
                print(k - 1)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)