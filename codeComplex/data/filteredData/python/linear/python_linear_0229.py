def main(n):
    # 生成确定性字符串：长度为 n，在 'x' 和 'a' 之间交替，并每隔 5 个位置插入两个连续的 'x'
    chars = []
    for i in range(n):
        if i % 5 == 0:
            chars.append('x')
        elif i % 5 == 1:
            chars.append('x')

        else:
            chars.append('a')
    s = ''.join(chars)

    count = 0
    temp_count = 0
    for c in s:
        if c == 'x':
            temp_count += 1

        else:
            temp_count = 0
        if temp_count == 3:
            count += 1
            temp_count -= 1

    return count


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值
    result = main(10)
    # print(result)
    pass