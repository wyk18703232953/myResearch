# coding: utf-8
import random

def main(n):
    # 生成测试数据：n 个点的“度数”
    # 这里生成 0~n-1 之间的随机整数作为度数示例，可按需要修改生成规则
    a = [random.randint(0, n - 1) for _ in range(n)]

    # 下面是原逻辑（去掉 input 和 sys.exit），并稍做封装
    arr = [[i, a[i]] for i in range(n)]
    arr.sort(key=lambda x: x[1], reverse=True)

    ans = []
    index = 0
    cnt = 0
    right_bool = False
    left_bool = False

    possible = True

    for i in range(1, n):
        if arr[index][1] == 0:
            possible = False
            break

        if arr[i][1] >= 2:
            ans.append([arr[i - 1][0], arr[i][0]])
            cnt += 1
            arr[i - 1][1] -= 1
            arr[i][1] -= 1
        else:
            if not right_bool:
                ans.append([arr[i - 1][0], arr[i][0]])
                arr[i - 1][1] -= 1
                arr[i][1] -= 1
                cnt += 1
                right_bool = True
            else:
                ans.append([arr[index][0], arr[i][0]])
                arr[index][1] -= 1
                arr[i][1] -= 1
                if not left_bool:
                    cnt += 1
                    left_bool = True
                if arr[index][1] == 0:
                    index += 1

    if not possible:
        print("NO")
        return

    print("YES", cnt)
    print(n - 1)
    for i in range(n - 1):
        print(ans[i][0] + 1, ans[i][1] + 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)