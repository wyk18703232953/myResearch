"""
    Second Order Statistics
"""
n = int(input())
sequence = [int(x) for x in input().split()]
firstOrderStatistics = min(sequence)
if sequence.count(firstOrderStatistics) == len(sequence):
    print("NO")
else:
    sequence = sorted(sequence)
    secondOrderStatistics = sequence[0]
    for i in sequence:
        if(i > secondOrderStatistics):
            secondOrderStatistics = i
            break
    print(secondOrderStatistics)