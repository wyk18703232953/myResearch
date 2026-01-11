def main(n):
    # 生成确定性的输入列表，长度为 n
    # 元素构造为 n-i，得到一个递减序列，符合原程序对降序排序的使用
    l = [n - i for i in range(n)]

    # 原始逻辑开始
    l.sort(reverse=True)
    coin = 0
    total_sum = sum(l)
    current_sum = 0
    for i in range(len(l)):
        coin += 1
        current_sum = current_sum + l[i]
        remaining_sum = total_sum - current_sum
        if current_sum > remaining_sum:
            break
    # print(coin)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模实验
    main(10)