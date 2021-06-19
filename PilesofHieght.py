'''
the basic algortihm idea is whenver i see the number diffrent form the current number, i would add, the number of 
numbers before that number
'''

def piles(heights):
    if len(heights)<2:
        return 0

    piles = sorted(heights,reverse=True)

    steps = 0
    for i in range(1,len(heights)):
        steps += i if heights[i-1] != heights[i] else 0

    return steps

s = [5,2,1]
print(piles(s))
