import random

def main(n: int):
    # 3. 根据 n 生成测试数据：生成 n 个随机整数
    values = [random.randint(0, 1000000) for _ in range(n)]

    wrong = 0
    sorted_values = sorted(values)
    for i in range(n):
        if values[i] != sorted_values[i]:
            wrong += 1
    if wrong > 2:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)