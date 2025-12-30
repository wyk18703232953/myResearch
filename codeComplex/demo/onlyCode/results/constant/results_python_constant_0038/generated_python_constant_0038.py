import random

def main(n: int) -> None:
    # 生成一个规模为 n 的测试数据，这里简单设为 2*n 的整数
    i = 2 * n

    # 原逻辑：对输入 i 进行 int(i/2) * 3 的计算并输出
    print(int(i / 2) * 3)

if __name__ == "__main__":
    # 示例调用，实际使用时可按需调用 main
    main(10)