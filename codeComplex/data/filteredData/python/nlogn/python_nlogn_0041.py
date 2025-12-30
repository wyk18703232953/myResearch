import random

def main(n):
    # 生成测试数据：长度为 n 的数组，元素为 1 到 10 之间的随机整数
    a = [random.randint(1, 10) for _ in range(n)]

    temp = max(a)
    if len(set(a)) == 1 and a[0] == 1:
        # 若全为 1，则将最后一个改为 2 并输出
        result = a[:-1] + [2]
    else:
        # 否则将最大值中的一个改为 1，并排序输出
        a[a.index(temp)] = 1
        a.sort()
        result = a

    print(*result)


# 示例调用
if __name__ == "__main__":
    main(5)