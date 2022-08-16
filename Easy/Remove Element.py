# ------------------------------------------------Q4) Remove Element--------------------------------------------
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

#  cases: 113 , Runtime: 16 ms, Memory Usage: 13.2 MB

nums = [2,2,2,2,5,3,6,8,3]
val = 2
i=0
while i<len(nums):
    if(nums[i] == val):
        nums.pop(i)
        i=0
    else:
        i +=1

print(nums)