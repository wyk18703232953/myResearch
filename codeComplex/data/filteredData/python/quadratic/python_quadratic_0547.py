def main(n):
    # 生成长度为 n 的确定性字符串 s
    # 使用简单规则：索引为偶数时为 '+', 奇数时为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    # 原程序的第一段逻辑：找到满足条件的最小 i
    limit = n  # 使用传入的 n 作为原程序中的 n 上界
    answer_i = limit
    for i in range(limit + 1):
        flag = True
        stones = i
        for ch in s:
            if ch == '-':
                if stones > 0:
                    stones -= 1
                else:
                    flag = False
                    break
            else:
                stones += 1
        if flag:
            answer_i = i
            break

    # 原程序的第二段逻辑：以找到的 i 作为初始 stones 再跑一遍
    stones = answer_i
    for ch in s:
        if ch == '-':
            stones -= 1
        else:
            stones += 1

    print(stones)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)