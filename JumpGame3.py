'''
A graph can be be traversed in 3 ways, bfs(queue), dfs with recurrsion, dfs with stack in this question we are going
to use dfs with stack
'''

def jumpGame(arr,start):

    stack,visited = [start],set()
    n = len(arr)


    while stack:
        pos = stack.pop()
        if arr[pos]==0:
            return True
        visited.add(pos)

        left,right = pos-arr[pos],pos+arr[pos]

        if left>=0 and left not in visited: stack.append(left)
        if right<n and right not in visited: stack.append(right)

    return False


arr = [4,2,3,0,3,1,2]
start = 5

print(jumpGame(arr,start))