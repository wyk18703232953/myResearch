import random

def main(n):
    # 1. 生成测试数据：原代码中实际读取的是 n'，然后令 n = n' + 1
    #    这里反推原始输入值 input_n，使得逻辑保持一致
    #    原：n = int(stdin.readline()) + 1
    #    现：给定规模 n，作为原始输入 input_n
    input_n = n

    # 2. 按照原始程序逻辑：n = input_n + 1
    n_val = input_n + 1

    # 3. 原始逻辑
    if n_val == 1:
        print(0)
    else:
        print(n_val // 2 if n_val % 2 == 0 else n_val)

if __name__ == "__main__":
    # 示例：给定规模 n = 10，可按需修改或在外部调用 main(n)
    main(10)