# 1195B.py

'''
有两种操作：
1. -1（吃掉一颗糖）
2. +x（放入x颗糖），x最开始为1，每做一次2操作，x+=1
现在给定操作的次数n和最终结果k
问做了1操作的次数（吃掉的糖的个数）
'''

def cal(x, n):
    return (1 + n - x) * (n - x) // 2 - x

n, k = map(int, input().strip().split())
low, hgh, mid = 0, n, -1
while low <= hgh:
    mid = (low + hgh) // 2
    cm = cal(mid, n)
    if cm == k:
        print(mid)
        break
    elif cm > k:
        low = mid + 1
    else:
        hgh = mid - 1