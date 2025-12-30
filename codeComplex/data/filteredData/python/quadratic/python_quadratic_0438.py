import random

def main(n):
    # 生成测试数据：长度为 n 的 0/1 数组（可按需要修改生成方式）
    arr = [random.randint(0, 1) for _ in range(n)]

    ans = 0

    if n == 2:
        if arr[0] == arr[1]:
            print("YES")
        else:
            print("NO")
        return

    for l in range(1, n - 1):
        s = sum(arr[:l])
        i = l
        v = [s]
        curr = 0
        while i < n:
            curr += arr[i]
            if i == n - 1:
                if curr > s:
                    curr -= arr[i]
                    v.append(curr)
                    curr = arr[i]
                v.append(curr)
            elif curr > s:
                curr -= arr[i]
                v.append(curr)
                curr = arr[i]
            i += 1

        if len(set(v)) == 1:
            print("YES")
            ans = 1
            return

    if not ans:
        print("NO")