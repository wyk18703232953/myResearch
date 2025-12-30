import random

def main(n):
    # 生成测试数据：n个范围在[0, 10*n]的随机整数
    A = [random.randint(0, 10 * n) for _ in range(n)]

    # 去重并排序
    A = list(set(A))
    A.sort()

    # 输出第二小的数或"NO"
    if len(A) > 1:
        print(A[1])
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可以在此修改n进行测试
    main(10)