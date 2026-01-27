def f(a, b):
    global ans
    maks = max(a, b)
    mins = min(a, b)
    ans += (maks // mins)
    if mins == 1:
        return ans

    else:
        if maks % mins == 0:
            return ans

        else:
            return f(maks % mins, mins)


def main(n):
    global ans
    results = []
    # 生成 n 组确定性测试数据 (a, b)
    # a 和 b 随 n 增大而增大，且 a,b >= 1
    for i in range(1, n + 1):
        a = i + 1
        b = 2 * i + 1
        ans = 0
        results.append(f(a, b))
    return results


if __name__ == "__main__":
    # 示例调用：可修改 n 来控制规模
    res = main(10)
    for v in res:
        # print(v)
        pass