def solve_value(x: int):
    arr = []
    while x > 0:
        arr.append(x % 2)
        x //= 2
    return arr

def main(n: int):
    """
    n: 控制生成测试数据 (l, r) 的规模参数
    这里简单设置：
      l = max(1, n)
      r = 2 * n + 1
    可根据需要自定义生成方式。
    """
    # 生成测试数据
    l = max(1, n)
    r = 2 * n + 1

    arrl = solve_value(l)
    arrr = solve_value(r)
    if len(arrr) > len(arrl):
        ans = (1 << len(arrr)) - 1
        print(ans)
    else:
        ind = -1
        for i in range(len(arrr) - 1, -1, -1):
            if arrr[i] != arrl[i]:
                ind = i
                break
        if ind == -1:
            print(0)
        else:
            ans = (1 << (ind + 1)) - 1
            print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)