def main(n):
    """
    规模 n 用来生成 (z, x) 测试数据。
    这里简单约定：
    - x = n
    - z 取一个 0 到 x*(x+1)//2 之间的值（例如 z = x*(x+1)//3 截断）
    可根据需要自行调整生成方式。
    """

    x = n
    # 确保 x >= 1
    if x <= 0:
        return

    # 生成 z，保证 0 <= z <= x*(x+1)//2
    total = x * (x + 1) // 2
    z = total // 3  # 随意选择一个不太极端的 z

    # 以下为原始逻辑（去掉 input 和 sys.exit）
    z -= 1
    x -= 1

    if x * (x + 1) / 2 < z:
        print(-1)
    elif z == 0:
        print(0)
    elif z == x:
        print(1)
    else:
        start = 1
        end = x
        while end > start:
            mid = (end + start) // 2
            ans = (x * (x + 1) // 2) - ((mid - 1) * mid // 2)
            if ans == z:
                print(x - mid + 1)
                break
            elif ans > z:
                start = mid + 1
            else:
                end = mid
        else:
            # while 未被 break 正常结束时执行
            print(x - end + 2)


# 如果需要在本文件直接运行测试，可以取消下方注释：
# if __name__ == "__main__":
#     main(10)