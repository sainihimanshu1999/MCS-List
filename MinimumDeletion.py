'''
Minimum deletion to make the characted frequency unique in string
'''

from collections import Counter

def minimumDeletion(s):
    count = Counter(s)
    result,used = 0,set()

    for char,freq in count.items():
        while freq>0 and freq in used:
            freq -=1
            result +=1

        used.add(freq)

    return result


s = "abbbcc"
print(minimumDeletion(s))

