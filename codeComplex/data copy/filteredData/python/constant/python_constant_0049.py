def main(n: int):
    # 根据规模 n 生成测试数据，这里直接使用参数 n 作为测试值
    k = set("47")
    p = False
    for i in range(1, n + 1):
        if n % i == 0:
            if set(str(i)) <= k:
                p = bool(set(str(i)))
                break
    if p:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：可自行修改 n 用于测试
    main(100)