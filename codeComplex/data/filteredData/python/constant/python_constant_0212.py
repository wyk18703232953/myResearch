import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的整数数组，元素范围 1~4
    a = [random.randint(1, 4) for _ in range(n)]

    if (a.count(1) >= 1 or
        a.count(2) >= 2 or
        a.count(3) == 3 or
        (a.count(2) == 1 and a.count(4) == 2)):
        print("YES")
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    main(10)  # 可修改 n 测试不同规模