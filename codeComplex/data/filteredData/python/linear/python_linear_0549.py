import sys

def main(n):
    # n 作为数组长度
    if n <= 0:
        print(-1)
        return
    a = [i // 2 for i in range(1, n + 1)]
    mx = 0
    for i in range(len(a)):
        if a[i] > mx:
            print(i + 1)
            return
        mx = max(mx, a[i] + 1)
    print(-1)

if __name__ == "__main__":
    main(10)