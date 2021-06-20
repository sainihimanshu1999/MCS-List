'''
it is a pretty easy question you just have to decode the formula of A[i] = i*2 -n+1
'''

def unique(n):
    res = []
    for i in range(n):
        res.append(i*2-n+1)
    return res

def unique2(n):
    return range(1-n,n,2)

print(unique2(5))