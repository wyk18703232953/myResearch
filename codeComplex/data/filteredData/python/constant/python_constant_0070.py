import random

def main(n):
    # 根据 n 生成测试数据（这里简单示例：生成一个长度为 n 的随机整数数组）
    test_data = [random.randint(0, 100) for _ in range(n)]
    
    # 原始逻辑：输出 "0 0 n"
    print("0", "0", n)

    # 如需使用测试数据，可在此处添加处理逻辑
    # 例如：打印测试数据（示例，实际可按需求修改）
    # print(test_data)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改 n 的值
    main(10)