import random

def main(n):
    # 生成测试数据：随机生成 t 组测试，每组长度为 1..n
    t = n
    test_cases = []
    for _ in range(t):
        length = random.randint(1, n)
        # 生成数组元素，范围自定，这里设为 1..n
        arr = [random.randint(1, n) for _ in range(length)]
        test_cases.append(arr)

    # 执行原逻辑
    for a in test_cases:
        length = len(a)
        if length == 1:
            print(0)
        else:
            max1 = max2 = -1
            for q in a:
                if q > max1:
                    max1, max2 = q, max1
                elif q > max2:
                    max2 = q
            print(max(0, min(max2 - 1, length - 2)))


if __name__ == "__main__":
    # 示例调用，可自行修改 n
    main(5)