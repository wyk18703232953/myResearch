def main(n):
    # 确定性生成长度为 n 的数组 a
    # 这里构造为 a[i] = i // 2，既包含重复又是单调不减，适合时间复杂度实验
    a = [i // 2 for i in range(n)]

    mx = -1
    ans = -1
    for i in range(n):
        if a[i] > mx + 1:
            ans = i + 1
            break
        else:
            mx = max(mx, a[i])
    print(ans)


if __name__ == "__main__":
    # 示例调用：可以按需要修改 n 的大小做实验
    main(10)