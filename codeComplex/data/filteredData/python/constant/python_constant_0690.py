import math
import random

def main(n: int):
    """
    n: 规模，用于生成测试数据
    这里约定：
      - 几何中的 n 为一个 >= 3 的整数
      - r 为一个 > 0 的半径，随规模生成
    """
    if n < 3:
        raise ValueError("n 必须 >= 3")

    # 根据规模 n 生成测试数据：
    # 几何意义的 n 取 main 的 n
    n_geom = n

    # 半径 r 随机生成，也可以换成其它生成方式
    # 这里让 r 与 n 同量级，范围 [1, n]
    random.seed(n)  # 固定种子，便于复现
    r = random.uniform(1.0, float(n))

    s = math.sin(math.pi / n_geom)
    ans = (r * s) / (1 - s)

    print(f"{ans:.7f}")


if __name__ == "__main__":
    # 示例：调用 main，规模可以自行修改
    main(10)