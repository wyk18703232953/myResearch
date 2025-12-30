def number(pos):
    ans = 0
    for i in range(pos + 1):
        ans += 2 ** i
    return ans

def main(n):
    # 生成测试数据：根据规模 n 构造 l, r
    # 示例策略：让 r - l = n，且 l 从 n 开始
    l = n
    r = n + n

    if l == r:
        print(0)
    else:
        b_pos = 0
        i = 0
        while l > 0 or r > 0:
            if (l % 2) != (r % 2):
                b_pos = i
            l >>= 1
            r >>= 1
            i += 1
        print(number(b_pos))

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)