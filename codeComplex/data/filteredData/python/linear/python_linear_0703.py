def main(n):
    # 生成长度为 n 的确定性字符序列，由 '+' 和 '-' 组成
    # 规则：索引为偶数位置为 '+', 奇数位置为 '-'
    a = ['+' if i % 2 == 0 else '-' for i in range(n)]
    x = 0
    for ch in a:
        if ch == '-':
            x = max(0, x - 1)

        else:
            x += 1
    return x

if __name__ == "__main__":
    # print(main(10))
    pass