''' 25A - IQ test '''
try:
    odd, even, oddIndex, evenIndex = 0, 0, 0, 0
    n = int(input())
    s = list(map(int, input().split()))
    counter = 0
    for i in s:
        if i % 2 == 0:
            even += 1
            evenIndex = counter
        else:
            odd += 1
            oddIndex = counter
        counter += 1
    ans = evenIndex + 1 if even == 1 else oddIndex + 1
    print(ans)
except EOFError as e:
    pass