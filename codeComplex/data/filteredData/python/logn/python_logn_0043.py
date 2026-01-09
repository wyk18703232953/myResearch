def main(n):
    # 根据规模 n 生成测试数据，这里示例为：
    # l = 0, r = n
    l, r = 0, n

    ans = l ^ r
    x = bin(ans)[1:]
    if ans == 0:
        # print(0)
        pass

    else:
        ptr = -1
        po = 0
        while True:
            if x[ptr] == '0':
                ans += 2 ** po
            po += 1
            ptr -= 1
            if ptr == -len(x) - 1:
                break

        # print(ans)
        pass
if __name__ == "__main__":
    # 示例调用
    main(10)