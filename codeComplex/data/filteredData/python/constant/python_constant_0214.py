import random

def main(n):
    # 根据规模 n 生成测试数据：生成 3 个 1~n 之间的整数
    l = [random.randint(1, n) for _ in range(3)]
    l.sort()
    x1, x2, x3 = l

    if x1 == 1 or (x1 == 2 and x2 == 4 and x3 == 4) or (x1 == 3 and x2 == 3 and x3 == 3) or (x1 == 2 and x2 == 2):
        print("YES")
    else:
        print("NO")

# 示例调用
if __name__ == "__main__":
    main(10)