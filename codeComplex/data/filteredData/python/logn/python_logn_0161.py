def main(n: int):
    # 根据规模 n 生成一组 (z, x) 测试数据
    # 这里约定：x = n，z 为一个在合法范围 [0, x*(x+1)//2] 内的值
    x = n
    # 简单构造：让 z 取大约一半的总和，保证通常走到二分逻辑
    total = x * (x + 1) // 2
    z = total // 2

    # 原逻辑开始
    z -= 1
    x -= 1

    if x * (x + 1) / 2 < z:
        # print(-1)
        pass
    elif z == 0:
        # print(0)
        pass
    elif z == x:
        # print(1)
        pass

    else:
        start = 1
        end = x
        while end > start:
            mid = (end + start) // 2
            ans = (x * (x + 1) // 2) - ((mid - 1) * mid // 2)
            if ans == z:
                # print(x - mid + 1)
                pass
                return
            elif ans > z:
                start = mid + 1
            else:  # ans < z
                end = mid
        # print(x - end + 2)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)