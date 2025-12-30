import random

def main(n):
    # 生成测试数据：长度为 n 的随机整数数组
    # 数值范围可按需调整
    a = [random.randint(1, 100) for _ in range(n)]
    print("Generated array:", a)

    b = sorted(a)

    diffs = []
    for i in range(n):
        if a[i] != b[i]:
            diffs.append(i)

    if len(diffs) > 2:
        print("NO")
    elif not diffs:
        print("YES")
    else:
        i, j = diffs
        if a[i] == b[j] and b[i] == a[j]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)