def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

original = input()
received = input()

originalNum = original.count('+') - original.count('-')
receivedNum = received.count('+') - received.count('-')

variance = received.count('?')

difference = abs(originalNum - receivedNum)

if variance==0:
    if difference==0:
        print(1.)
    else:
        print(0.)
elif difference > variance or difference%2!=variance%2:
    print(0.)
else:
    difference += variance
    difference//=2

    c = factorial(variance)/(factorial(difference)*factorial(variance-difference))
    print(c/(2**variance))

