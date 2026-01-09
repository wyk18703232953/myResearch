def main(n: int):
    # 根据规模 n 直接作为测试数据使用
    if n == 0:
        # print(*[0, 0, 0])
        pass
    elif n == 1:
        # print(*[0, 0, 1])
        pass

    else:
        prev2 = 0
        prev1 = 1
        prev = 1
        while prev != n:
            curr = prev + prev1
            prev2 = prev1
            prev1 = prev
            prev = curr
        # print(*[0, prev2, prev1])
        pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 的测试值
    main(10)