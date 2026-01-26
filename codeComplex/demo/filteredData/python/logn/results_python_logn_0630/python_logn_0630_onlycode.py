import math

def gaosi(x):
    if (x==1):
        return 1
    else:
        return ((1+x)*x)/2

def calc(mid, total, left):
    return gaosi(mid) - (total - mid) - left

def main(): 
    x, left = map(int, input().split())
    if (x == 1 and left == 1):
        print(0)
    else:
        l = 1
        r = x
        while (True):
            mid = math.floor((l + r) / 2)
            result = calc(mid, x, left)
            if (result == 0):
                print(x - mid)
                break
            elif (result > 0):
                r = mid
            elif (result  < left):
                l = mid

    
if __name__ == "__main__":
    main()