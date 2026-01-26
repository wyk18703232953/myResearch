import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math


def main():
    # something
    n = getN()
    nums = getList()
    nums.sort()
    margins = [num - i for i, num in enumerate(nums)]
    for m in margins:
        if m < 0:
            print("cslnb")
            return
    flag = False
    if len(nums) > 1:
        if nums[0] == nums[1]:
                flag = True
    for a, b, c in zip(nums, nums[1:], nums[2:]):
        if b == c:
            if a == b or b - a == 1:
                print("cslnb")
                return
            if flag:
                print("cslnb")
                return
            flag = True


    # if nums[0] == 0 and nums[1] == 0:
    #     print("cslnb")
    #     return
    # print("duel")
    margin = sum(margins)
    # print(margin)
    # print(nums)
    if margin % 2 == 1:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    main()

