def main(n):
    # 生成确定性输入数组，长度为 n
    # 元素构造方式：i % (n // 2 + 1)，保证有重复且值范围可控
    A = [i % (n // 2 + 1) for i in range(n)]
    A = list(set(A))
    A.sort()
    if len(A) > 1:
        # print(A[1])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)