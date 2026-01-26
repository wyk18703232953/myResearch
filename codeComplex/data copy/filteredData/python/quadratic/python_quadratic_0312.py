import sys, heapq

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    k = max(1, n // 2)
    arr = [(i * 2 + 1) % (n + 3) for i in range(n)]
    pf = [0] * (n + 1)
    if n > 0:
        pf[0] = arr[0]
    for i in range(1, n):
        pf[i] = pf[i - 1] + arr[i]
    ans = 0
    for i in range(n):
        for j in range(n):
            left = i
            right = j
            if right - left + 1 >= k:
                if left == 0:
                    temp = pf[right]

                else:
                    temp = pf[right] - pf[left - 1]
                avg = temp / (right - left + 1)
                if avg > ans:
                    ans = avg
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)