import random

def main(n):
    # 生成测试数据：a 为长度为 n 的数组，元素范围 [1, n]
    a = [random.randint(1, n) for _ in range(n)]
    ans = [None] * n

    def get(p):
        if ans[p] is not None:
            return ans[p]
        elif a[p] == 1:
            ans[p] = "A"
        elif a[p] == n:
            ans[p] = "B"
        else:
            step = a[p]
            # 向右跳
            for i in range(p + step, n, step):
                if a[i] > a[p]:
                    if get(i) == "B":
                        ans[p] = "A"
                        return ans[p]
            # 向左跳
            for i in range(p - step, -1, -step):
                if a[i] > a[p]:
                    if get(i) == "B":
                        ans[p] = "A"
                        return ans[p]
            ans[p] = "B"
        return ans[p]

    if n == 1:
        print("B")
    else:
        for i in range(n - 1, -1, -1):
            get(i)
        print(''.join(ans))

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)