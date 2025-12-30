import random

def main(n):
    """
    n 为测试规模，用来控制生成测试数据的范围。
    按原逻辑：读一个字符串 a，将其转为 int 后加 1 得到 b，再根据 b 输出结果。
    这里根据 n 生成测试数据 a：在 [-n, n] 区间随机取一个整数并转为字符串。
    """
    # 1. 根据 n 生成测试数据 a
    if n <= 0:
        # 若 n 非正，就固定用 0，避免随机区间非法
        x = 0
    else:
        x = random.randint(-n, n)
    a = str(x)

    # 2. 按原逻辑处理
    b = int(a) + 1
    if b == 1:
        print("0")
    elif b % 2 == 0:
        print(b // 2)
    elif b % 2 != 0:
        print(b)

# 示例：需要时可以调用 main(n)
# main(10)