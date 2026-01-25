def substring(x, s):
    count = 0
    ans = 0
    for i in range(x):
        if s[i] == "x":
            count += 1
        else:
            if count >= 3:
                ans += count - 2
            count = 0
    if count >= 3:
        ans += count - 2
    return ans

def main(n):
    # n 表示字符串长度
    if n <= 0:
        print(0)
        return
    # 构造一个确定性的字符串：
    # 规则：位置 i (从 0 开始)，如果 i % 3 != 0 则为 'x'，否则为 'y'
    s = "".join("x" if i % 3 != 0 else "y" for i in range(n))
    x = len(s)
    result = substring(x, s)
    print(result)

if __name__ == "__main__":
    main(10)