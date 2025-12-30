import random

def main(n: int):
    # 生成测试数据：长度为 n 的 0/1 串 a_str 和 b_str
    # 这里随机生成，你也可以按需改成特定模式
    a = [random.randint(0, 1) for _ in range(n)]
    b = [random.randint(0, 1) for _ in range(n)]

    # 转换为布尔列表，保持与原程序逻辑一致：True 表示 '1'
    a_bool = [x == 1 for x in a]
    b_bool = [x == 1 for x in b]

    res = 0
    i = 0
    while i + 1 < n:
        if (
            a_bool[i] != b_bool[i]
            and a_bool[i] != a_bool[i + 1]
            and b_bool[i] != b_bool[i + 1]
        ):
            a_bool[i] = b_bool[i]
            a_bool[i + 1] = b_bool[i + 1]
            res += 1
            i += 2
        else:
            i += 1

    for i in range(n):
        if a_bool[i] != b_bool[i]:
            res += 1

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)