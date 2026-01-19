def factorial(n) :
    ans = 1
    if (n == 0) :
        return 1
    for i in range(1, n + 1) :
        ans *= i
    return ans
def ncr(n , r) :
    n = abs(n) 
    if r > n :
        return 0 
    ans = factorial(n)
    ans = ans//(factorial(n-r)) 
    ans = ans//(factorial(r))
    return ans

if __name__ == "__main__" :
    A = input() 
    B = input()
    QMarks = B.count('?')   
    TotalA = A.count('+') - A.count('-') 
    TotalB = B.count('+') - B.count('-') 
    denominator = 2**QMarks
    if QMarks < abs(TotalA - TotalB) :  
        print(0) 
    else :
        x = (QMarks - abs(TotalA - TotalB))//2
        x += abs(TotalA - TotalB)
        num = ncr(QMarks,x) 
        print(num/denominator)