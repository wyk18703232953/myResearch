def main(n):
    # 映射含义：
    # n -> 输入数组 p 的长度
    # k -> 取一个与 n 有确定关系的值，保证可扩展且可复现实验
    if n <= 0:
        return

    # 合理设定 k：与 n 同量级，且至少为 1
    k = max(1, n // 2)

    # 构造确定性的 p：长度为 n，元素落在 [0, 255] 范围内
    # 使用简单算术构造，避免非确定性
    p = [(i * 7 + 3) % 256 for i in range(n)]

    arr = [[] for _ in range(256)]
    ans = []
    for i in p:
        j = i
        if len(arr[i]) == 0:
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
    # print(*ans)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行时间复杂度实验
    main(10)