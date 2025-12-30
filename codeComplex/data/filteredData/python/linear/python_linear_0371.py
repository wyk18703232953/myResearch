import random

def main(n):
    # 生成规模为 n 的测试数据
    # 假设 m 与 n 同级，这里设置 m = n，也可以根据需要修改为其他函数关系
    m = n

    # 生成价格列表 c（例如 1~100 的随机整数）
    c = [random.randint(1, 100) for _ in range(n)]

    # 生成预算列表 a（例如 1~100 的随机整数），长度为 m
    a = [random.randint(1, 100) for _ in range(m)]

    # 原逻辑开始
    c_i = 0
    a_i = 0
    bought = 0
    while c_i != n and a_i != m:
        if a[a_i] >= c[c_i]:
            a_i += 1
            c_i += 1
            bought += 1
        else:
            c_i += 1

    print(bought)

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)