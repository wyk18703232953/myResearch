def main(n):
    # 生成测试数据，这里直接使用 n 作为待检测的数
    s = n

    u = True
    for i in [4, 7, 47, 74, 447, 474, 477, 747, 774]:
        if s % i == 0:
            u = False
            # print("YES")
            pass
            break
    if u:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：可在此处修改 n 以进行测试
    main(28)