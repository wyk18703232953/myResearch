import random

def main(n):
    # 生成测试数据：长度为 n 的整数列表，值在 1~n 之间
    l = [random.randint(1, n) for _ in range(n)]

    # 原逻辑
    l.sort()
    for x in range(1, n):
        if l[x] > l[0]:
            print(l[x])
            break
    else:
        print('NO')

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)