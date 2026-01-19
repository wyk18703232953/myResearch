import math

def sequence_split_up(sequence):
    ans=[0,0,0]
    for i in sequence:
        if i=='+':
            ans[0]+=1
        elif i=='-':
            ans[1]+=1
        elif i=='?':
            ans[2]+=1
    return ans
    
def probability():
    actual_sequence=sequence_split_up(drazil_send)
    sequence_received=sequence_split_up(dreamoon_received)
    total_len=sum(actual_sequence)
    actual_ans=actual_sequence[0]-actual_sequence[1]
    ans_received=sequence_received[0]-sequence_received[1]
    difference=actual_ans-ans_received
    no_of_blanks=sequence_received[2]
    if no_of_blanks==0:
        if actual_ans!=ans_received:
            return 0
        return 1
    if abs(difference)>no_of_blanks:
        return 0
    ans_set=[0,0]
    if difference>0:
        ans_set[0]+=difference
    elif difference<0:
        ans_set[1]+=abs(difference)
    blanks_left=no_of_blanks-abs(difference)
    ans_set[0]=ans_set[0]+blanks_left//2
    ans_set[1]=ans_set[1]+blanks_left//2
    x = (math.factorial(no_of_blanks)//(math.factorial(ans_set[0])*math.factorial(ans_set[1])))/math.pow(2,no_of_blanks)
    return x
    
    
drazil_send=input()
dreamoon_received=input()
print("%.12f"%probability())
