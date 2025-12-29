import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组，元素范围可根据需要调整
    # 这里假设元素范围为 [-n, n]
    a_list = [random.randint(-n, n) for _ in range(n)]
    a = set(a_list)

    ans = len(a) - 1 if 0 in a else len(a)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)