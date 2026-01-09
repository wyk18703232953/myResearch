def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 构造方式：重复模式 [0,1,2,3,4]，保证存在重复元素，避免 index 出错
    if n <= 1:
        xs = [0, 0]  # 保证至少一个可匹配对

    else:
        xs = [i % 5 for i in range(n)]
        # 确保首元素在后面至少再出现一次
        if xs.count(xs[0]) == 1:
            xs[0] = xs[-1]

    res = 0
    while len(xs) > 1:
        # 寻找和首元素相同的下一个元素位置
        j = xs.index(xs[0], 1)
        res += j - 1
        xs = xs[1:j] + xs[j+1:]

    return res


if __name__ == "__main__":
    # 示例调用
    for n in [2, 5, 10, 20]:
        # print(n, main(n))
        pass