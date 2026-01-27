def main(n):
    # 根据 n 构造三个整数，确定性生成
    # 映射方式：三个数围绕 n 做简单变换
    l = [n, n // 2 + 1, (n % 5) + 1]
    l.sort()
    if l[0] == 1 or (l[0] == 2 and l[1] == 4 and l[2] == 4) or (l[0] == 3 and l[1] == 3 and l[2] == 3) or (l[0] == 2 and l[1] == 2):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)