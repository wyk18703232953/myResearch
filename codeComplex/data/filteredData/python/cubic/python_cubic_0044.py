def main(n):
    # 生成确定性字符串：周期性地使用小写字母
    # 字符串长度由 n 决定
    if n <= 0:
        x = ""

    else:
        x = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    a = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i:j] in x[i+1:]:
                if len(x[i:j]) > a:
                    a = len(x[i:j])
    # print(a)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)