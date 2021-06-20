'''
Largest integer k, such as k aand -k both present in array
'''

def finding(nums):
    left,right = 0,len(nums)-1
    nums = sorted(nums)

    while left<right:
        if nums[left]+nums[right]==0:
            return nums[right]
        elif abs(nums[left])>nums[right]:
            left+=1
        else:
            right -=1
    return 0

print(finding([3, 2, -2, 5, -3]))


