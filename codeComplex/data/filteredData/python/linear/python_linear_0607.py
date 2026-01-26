def main(n):
    # 第一段循环：范围由 n//3 决定
    for i in range(n // 3):
        # print(-2, 1 + i * 2)
        pass
    # 第二段循环：范围由 n - n//3 决定
    for i in range(n - n // 3):
        # print(1, i)
        pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值进行时间复杂度实验
    main(10)