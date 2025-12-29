import random

def main(n: int) -> int:
    """
    n: 规模，对应原程序中的行数
    返回值: 对应原程序最终输出的 r
    """
    # 生成测试数据：
    # 每行生成 3 个 0~9 的随机整数，可以根据需要调整生成规则
    data = [[random.randint(0, 9) for _ in range(3)] for _ in range(n)]

    # 以下是原逻辑的无 input 实现
    r = 1
    t = sum(data[0])
    for i in range(1, n):
        if sum(data[i]) > t:
            r += 1

    return r

if __name__ == "__main__":
    # 示例调用：规模设为 5
    result = main(5)
    print(result)