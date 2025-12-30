import random

def main(n: int):
    # 3. 生成长度为 n 的测试数据 a，这里生成 0 到 n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    mx = -1
    for step, elem in enumerate(a):
        if elem > mx + 1:
            print(step + 1)
            return
        else:
            mx = max(mx, elem)
    print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)