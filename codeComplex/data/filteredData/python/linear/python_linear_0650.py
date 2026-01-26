def main(n):
    # 确定性生成输入
    # 设定 c 为一个固定值
    c = 5
    # 生成长度为 n 的数组
    # 按照简单规则构造：部分是 c，部分是其他值
    arr = [(i % 7) + 1 for i in range(n)]
    # 让数组中有一定比例为 c
    for i in range(0, n, 3):
        arr[i] = c

    cnt = [0] * 500005
    ans = 0

    for v in arr:
        if v == c:
            cnt[c] = cnt[c] + 1

        else:
            if cnt[v] < cnt[c]:
                cnt[v] = cnt[c]
            cnt[v] += 1
        ans = max(ans, cnt[v] - cnt[c])

    result = ans + cnt[c]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做实验
    main(10)