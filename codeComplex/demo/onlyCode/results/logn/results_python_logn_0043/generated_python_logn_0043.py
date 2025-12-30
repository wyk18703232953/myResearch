def main(n: int):
    # 根据规模 n 生成测试数据，这里生成一个区间 [l, r]，使得 r - l = n
    l = 0
    r = n

    ans = l ^ r
    x = bin(ans)[1:]
    if ans == 0:
        print(0)
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

        print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)