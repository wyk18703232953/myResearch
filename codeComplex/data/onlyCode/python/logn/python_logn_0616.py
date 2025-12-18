'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

tot, choc = [int(i) for i in input().split()]

# add = 0
# mid = tot
bg = 1
end = tot

while True:
    mid = (bg + end) / 2
    add = (mid * (mid + 1)) / 2
    sub = tot - mid
    if add - sub == choc:
        print(int(sub))
        break
    if add - sub < choc:
        bg = mid + 1
    else:
        end = mid - 1
    
