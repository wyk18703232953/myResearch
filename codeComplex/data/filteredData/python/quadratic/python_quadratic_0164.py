import random

def main(n):
    # 随机生成一个适配规模 n 的 k（至少为 1）
    # 原代码里 k 来自输入，这里简单设为 1~n 之间的随机值
    k = random.randint(1, max(1, n))

    # 随机生成长度为 n 的 p 数组，元素范围适配原代码的 arr 长度 256
    # 若希望完全复现原逻辑，可保证所有元素在 [0, 255] 内
    p = [random.randint(0, 255) for _ in range(n)]

    arr = [[] for _ in range(256)]
    ans = []
    for i in p:
        if len(arr[i]) == 0:
            j = i
            c = 0
            while c < k and j >= 0:
                if len(arr[j]) + c > k:
                    break
                if len(arr[j]) != 0:
                    arr[i].extend(arr[j])
                    break
                arr[j] = arr[i]
                arr[j].append(j)
                j -= 1
                c += 1
            arr[i].sort()
        ans.append(arr[i][0])

    # 输出与原程序一致的格式
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)