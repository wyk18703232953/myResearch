def forninho(miolo, s):
    premiolo = miolo
    temp = 0
    while miolo > 0:
        temp += miolo % 10
        miolo = miolo // 10
    if premiolo - temp >= s:
        return 1
    else:
        return 0


def main(n):
    # 根据 n 生成测试数据：
    # 这里假设 s 为规模的一半，可按需调整生成规则
    s = n // 2

    result = -1
    l = 1
    r = n
    while r - l >= 0:
        miolo = (l + r) // 2
        if forninho(miolo, s) == 1:
            r = miolo - 1
            result = miolo
        else:
            l = miolo + 1

    if result == -1:
        print("0")
    else:
        print(n - result + 1)


# 示例：运行 main(100) 进行测试
if __name__ == "__main__":
    main(100)