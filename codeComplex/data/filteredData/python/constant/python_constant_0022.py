import random

def main(n: int):
    # 根据 n 生成测试数据，这里原代码只需要一个整数 n
    # 可根据需要修改为其他生成方式，例如随机或固定规则
    generated_n = n  # 保持行为一致：直接使用传入的规模 n

    # 原始逻辑：对输入的 n 计算 3*n//2 后输出
    result = 3 * generated_n // 2
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模可以自行调整
    main(10)