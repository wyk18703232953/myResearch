import random

def main(n: int):
    # 根据规模 n 生成测试数据 A（随机整数列表）
    # 可根据需要修改生成规则，例如范围、分布等
    A = [random.randint(0, 1000) for _ in range(n)]

    B = A.copy()
    B.sort()
    c = 0
    for i in range(n):
        a = A[i]
        b = B[i]
        if a == b:
            continue
        else:
            c += 1
    if c == 0 or c == 2:
        print("YES")
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    main(10)