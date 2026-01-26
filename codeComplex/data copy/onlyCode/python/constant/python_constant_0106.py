import sys
if __name__=='__main__':
    # read input
    numCases = int(sys.stdin.readline())
    for i in range(numCases):
        a, b = sys.stdin.readline().split()
        a = int(a)
        b = int(b)
        total = 0
        largerNum = max(a,b)
        smallerNum = min(a,b)
        while True:
            div = int(largerNum/smallerNum)
            total += div
            rem = int(largerNum%(smallerNum*div))
            if rem == 0:
                break
            else:
                largerNum = smallerNum
                smallerNum = rem
                
        print(total)
        
    