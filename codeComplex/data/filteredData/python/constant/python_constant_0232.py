import random

def main(n):
    # n 作为规模参数，这里用于控制随机数据的范围
    # 生成测试数据：
    # A, B 为现有的黄色和蓝色球数量
    # yellow, green, blue 为需要制作的黄色、绿色、蓝色球数量
    max_val = max(1, n)  # 防止 n 为 0
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)
    yellow = random.randint(0, max_val)
    green = random.randint(0, max_val)
    blue = random.randint(0, max_val)

    # 原逻辑
    yelreq = 0
    blureq = 0

    # for yellow balls
    yelreq = 2 * yellow

    # green balls
    yelreq += green
    blureq += green

    # blue balls
    blureq += 3 * blue

    reqs = 0
    if A < yelreq:
        reqs += yelreq - A
    if B < blureq:
        reqs += blureq - B

    print(reqs)

# 示例调用
if __name__ == "__main__":
    main(10)