import math
import random

def main(n: int):
    """
    n 用作生成测试数据的规模参数：
    - 随机生成 no_of_moves ∈ [0, n]
    - 随机生成 no_of_candy ∈ [1, n]
    然后执行原逻辑。
    """
    # 生成测试数据
    if n <= 0:
        no_of_moves = 0
        no_of_candy = 1
    else:
        no_of_moves = random.randint(0, n)
        no_of_candy = random.randint(1, n)

    total_candy = now_candy = 1
    now_moves = 1

    if no_of_moves == 0 or (no_of_moves == 1 and no_of_candy == 1):
        print(0)
    else:
        while True:
            now_candy = now_candy + 1
            total_candy += now_candy
            now_moves += 1
            if total_candy - (no_of_moves - now_moves) == no_of_candy:
                break

        print(no_of_moves - now_moves)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)