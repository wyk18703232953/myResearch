import math
import random


def main(n: int) -> None:
    # 生成测试数据：
    # 原程序中：n, k = scan()
    # 这里保持 n 为规模参数，同时随机生成一个 k
    #
    # 为了让表达式在数学上合理，这里约束 k >= 0
    # 若需要其他分布，可以自行修改生成规则
    k = random.randint(0, max(0, 2 * n))

    # 原逻辑：
    # print(round(n+1.5-math.sqrt(2*(n+k)+2.75)))
    result = round(n + 1.5 - math.sqrt(2 * (n + k) + 2.75))
    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要调整 n
    main(10)