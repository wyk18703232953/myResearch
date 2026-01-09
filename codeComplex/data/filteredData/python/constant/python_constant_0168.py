def main(n):
    # 将 n 映射为 (x, y)，保证 y > x
    # 这里选择：x = 1，y = n + 2，使得规模随 n 线性增长
    x = 1
    y = n + 2

    if abs(x - y) < 2:
        # print(-1)
        pass

    else:
        k = []
        for i in range(x, y + 1):
            if i % 2 == 0:
                k.append(i)
                if i + 1 < y:
                    k.append(i + 1)
                    k.append(i + 2)
                    break
        if len(k) == 3:
            # print(" ".join(str(t) for t in k))
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做规模实验
    main(10)