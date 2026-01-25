def main(n):
    # n 表示字符串长度
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    stones = 0
    for c in s:
        if c == '+':
            stones += 1
        else:
            stones -= 1
            if stones < 0:
                stones = 0
    print(stones)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)