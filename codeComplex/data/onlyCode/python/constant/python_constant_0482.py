USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    n, k = map(int, input().split(' '))
    ans = (k + n - 1) // n
    print(ans)

if __name__ == '__main__':
    main()



