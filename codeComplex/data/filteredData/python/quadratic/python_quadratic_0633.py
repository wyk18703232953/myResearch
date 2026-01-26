def main(n):
    # n 表示数组长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成测试数据：长度为 n 的整数列表
    # 使用简单的算术构造，避免随机性
    a = [(i + 1) * (i // 2 + 1) for i in range(n)]

    a.sort(reverse=True)

    cnt = 0
    while a:
        f = a.pop()
        rm = []
        for x in a:
            if x % f == 0:
                rm.append(x)
        for x in rm:
            a.remove(x)
        cnt += 1

    # print(cnt)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)