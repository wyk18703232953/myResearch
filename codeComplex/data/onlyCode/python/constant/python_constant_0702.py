if __name__ == '__main__':    
    nums = input().split()
    n = int(nums[0])
    v = int(nums[1])

    if n < v+2:
        print(n - 1)
    else:
        print(int(v-1 + (n-v)*(n-v+1)/2))