def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    k = n
    # 确定性生成测试数据：z[i] = i + k * ((i % 3) - 1)
    z = [i + k * ((i % 3) - 1) for i in range(n)]

    ans = []
    for i in range(len(z)):
        if (z[i] - i) % len(z) == 0:
            ans.append((z[i] - i) // k)
        else:
            ans.append((z[i] - i) // k)
            ans[-1] += 1
    t = min(ans)
    print(ans.index(t) + 1)


if __name__ == "__main__":
    main(10)