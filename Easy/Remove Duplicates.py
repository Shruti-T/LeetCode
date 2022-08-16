
# -------------------------------------------Q3) Remove Duplicates----------------------------------------------
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 

# cases = 362,Runtime: 60 ms,Memory Usage: 15.2 MB

nums = [-1,-1,0,0]
ori = len(nums)
if (ori>0 ):
    nums.append(-101)
for i in range(0, ori):
    if (nums[i] != nums[i+1]):
        nums.append(nums[i])

del nums[0:ori+1]
print(nums)