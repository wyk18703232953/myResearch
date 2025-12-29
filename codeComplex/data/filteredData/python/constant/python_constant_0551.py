import random

def main(n: int):
    # 根据 n 生成测试数据，这里生成 s 为 [0, 10*n] 内的随机整数
    s = random.randint(0, 10 * n)
    # 原逻辑：输出 (s + n - 1) // n
    print((s + n - 1) // n)


# 示例调用（提交到OJ时可去掉或由外部调用 main(n)）
if __name__ == "__main__":
    # 可以根据需要修改 n 的取值
    main(10)