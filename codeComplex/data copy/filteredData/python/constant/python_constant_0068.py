def main(n):
    # 这里的 n 作为“输入规模”，我们将其映射为原程序中的输入值 x
    x = n
    if x == 0:
        print(*[0, 0, 0])
    elif x == 1:
        print(*[0, 0, 1])
    else:
        prev2 = 0
        prev1 = 1
        prev = 1
        # 原程序假设 x 出现在这个 Fibonacci 序列中
        while prev != x:
            curr = prev + prev1
            prev2 = prev1
            prev1 = prev
            prev = curr
        print(*[0, prev2, prev1])


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做时间复杂度实验
    main(10)