import random

def main(n: int):
    # 根据 n 生成测试数据：随机生成 s，保证 s >= 0
    # 这里令 s 在 [0, n * 10] 范围内随机
    s = random.randint(0, n * 10)

    big = s // n
    r = s - big * n
    if r > 0:
        print(big + 1)
    else:
        print(big)


# 示例调用（如需测试可取消注释）
# if __name__ == "__main__":
#     main(5)