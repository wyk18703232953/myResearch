import random

def main(n: int):
    # 根据 n 生成测试数据：长度为 n 的列表，每个元素为 1~4 之间的整数
    l = [random.randint(1, 4) for _ in range(n)]

    s1 = s2 = s3 = s4 = 0
    for i in l:
        if i == 1:
            s1 += 1
        if i == 2:
            s2 += 1
        if i == 3:
            s3 += 1
        if i == 4:
            s4 += 1

    if s3 > 2 or s2 > 1 or s1 > 0 or (s4 == 2 and s2 == 1):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：n = 10
    main(10)