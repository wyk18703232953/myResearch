def main(n):
    # 生成确定性的测试数据列表 a，长度为 n
    # 使用简单的算术模式来生成 1~5 之间的整数
    a = [(i % 5) + 1 for i in range(n)]

    if a.count(1) >= 1 or a.count(2) >= 2 or a.count(3) == 3 or (a.count(2) == 1 and a.count(4) == 2):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(10)