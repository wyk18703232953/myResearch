import random

def main(n):
    # 生成测试数据：k 在 [1, min(10, n)]，元素在 [0, 255]
    k = random.randint(1, max(1, min(10, n)))
    ls = [random.randint(0, 255) for _ in range(n)]

    ar = [-1 for _ in range(256)]

    for e in ls:
        if ar[e] == -1:
            tmp = max(0, e - k + 1)
            i = tmp
            while i <= e:
                if ar[i] != -1 and ar[i] != i:
                    tmp += 1
                    i = tmp
                    continue
                else:
                    while i <= e:
                        ar[i] = tmp
                        i += 1
                    break
        print(ar[e], end=" ")


if __name__ == "__main__":
    # 示例：n = 10
    main(10)