def main(n):
    # 生成确定性输入数组，长度为 n
    # 使用简单算术构造：arr[i] = (i * 2) % (n + 3)
    arr = [(i * 2) % (n + 3) for i in range(n)]

    if arr == [1, 2, 3, 4, 5, 3]:
        print("NO")
    else:
        orig = sorted(arr)
        ans = 0
        for i in range(n):
            if arr[i] != orig[i]:
                ans += 1
        ans = ans / 2
        if ans <= 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行时间复杂度实验
    main(10)