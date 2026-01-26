def main(n):
    # 通过确定性方式生成长度为 n 的数组 a
    # 示例构造：a[i] = i % (n // 2 + 1)
    a = [(i * 2 + 1) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]

    c = 0
    for i in range(n):
        if a[i] > c:
            # print(i + 1)
            pass
            break

        else:
            c = max(a[i] + 1, c)

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)