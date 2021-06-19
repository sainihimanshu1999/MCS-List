'''
A valid palindrome have at most 1 character with odd frequency
'''
from collections import Counter

def minswap(s):
    count = Counter(s)
    x = len([char for char,freq in count.items() if freq %2])

    if x>1:
        return -1


    s = list(s)

    left,right = 0,len(s)-1

    swaps = 0

    while left<right:
        #if two are equal we close the window
        if s[left]==s[right]:
            left+=1
            right-=1

        else:
            #we try to found the char on the righttmost side which matches the first
            mid = right
            
            while mid>left and s[left]!=s[mid]:
                mid -=1
            #if char not found, we end up in middle, the on with odd freq just replace
            if mid == left:
                s[mid],s[mid+1] = s[mid+1],s[mid]
                swaps +=1 
                continue
            #when we found the char
            for i in range(mid,right):
                s[i],s[i+1] = s[i+1],s[i]
                swaps +=1
            
            left+=1
            right-=1
    return swaps



s = "mamad"
print(minswap(s))

