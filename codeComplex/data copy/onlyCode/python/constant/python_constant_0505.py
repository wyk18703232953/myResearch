USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    q,  = map(int, input().split(' '))
    for _ in range(q):
        n, m, k = map(int, input().split(' '))
        if n > k or m > k:
            print(-1)
        elif (n - m) % 2:
            print(k - 1)
        elif (n - k) % 2:
            print(k - 2)
        else:
            print(k)

if __name__ == '__main__':
    main()



