from collections import Counter


def solve():
    n, k = tuple( map( lambda x: int(x), input().split()) )
    
    low, high = 0, n

    while low <= high:
        eaten = (low+high)//2
        added = (n-eaten)* (n-eaten+1)/2

        if added - eaten >= k:
            low = eaten + 1
        else:
            high = eaten - 1 

    print(high)

        

if __name__ == "__main__":
    solve()