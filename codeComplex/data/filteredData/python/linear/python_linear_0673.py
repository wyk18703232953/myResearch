def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 元素模式：a[i] = i % 3 保证有偶有奇，适合测试算法行为
    a = [i % 3 for i in range(n)]

    b = []
    for i in range(n):
        a[i] %= 2
        if len(b) != 0:
            if b[-1] == a[i]:
                b.pop()
            else:
                b.append(a[i])
        else:
            b.append(a[i])
    if len(b) > 1:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的规模做实验
    main(10)