def main(n):
    # 根据 n 确定性生成输入数据
    bx = n
    by = -n
    ax = n + 1
    ay = -n + 1
    cx = n + (n % 2)
    cy = -n + (n % 3)

    num1 = ax > bx
    num3 = cx > bx
    num2 = ay > by
    num4 = cy > by
    if num1 == num3 and num2 == num4:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)