'''
This question is one where you have to think a little bit deeply, we use two methods to solve this question, on is
iterative and otherone is recursive(dfs)
'''

#Iterative Method
def unique(s):

    max_len = 0
    result = ['']

    def isValid(s):
        return len(s) == len(set(s))

    for word in s:
        for j in result:
            temp = word+j
            if isValid(temp):
                result.append(temp)
                max_len = max(max_len,len(temp))

    return max_len


#Recursicve(DFS) method

def unique2(s):
    max_len = 0

    def dfs(x,index):
        nonlocal max_len
        if len(x) != len(set(x)):
            return
        
        max_len = max(max_len,len(x))

        for i in range(index,len(s)):
            dfs(x+s[i],index+1)

    if not s:
        return 0
    dfs('',0)
    return max_len



arr = ["un","iq","ue"]
print(unique2(arr))