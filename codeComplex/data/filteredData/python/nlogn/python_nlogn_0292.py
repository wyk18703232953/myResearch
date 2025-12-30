from random import randint

def main(n):
    # 1. 生成测试数据：长度为 n 的数组 arr（元素为 1..10^9 的随机整数）
    #    和长度为 n 的只含 '0'/'1' 的字符串 lst
    arr = [randint(1, 10**9) for _ in range(n)]
    lst = ''.join(str(randint(0, 1)) for _ in range(n))

    # 2. 原始逻辑开始
    new_arr = sorted((val, idx) for idx, val in enumerate(arr))

    stack = []
    ans = []

    size = 0
    left = 0
    right = n - 1

    for ch in lst:
        if ch == '0':
            ans.append(new_arr[left][1] + 1)
            stack.append(new_arr[left][1] + 1)
            size += 1
            left += 1

        if ch == '1':
            if size == 0:
                ans.append(new_arr[right][1] + 1)
                stack.append(new_arr[right][1] + 1)
                right -= 1
            else:
                ans.append(stack[-1])
                stack.pop()
                size -= 1

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)