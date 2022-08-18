# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# -----------------------------------SOLUTION-------------------------------
# cases = 209, Runtime: 709 ms ,Memory Usage: 28 MB
arr=[-2,1,-3,4,-1,2,1,-5,4]
sumA=0
maxA=arr[0]
for i in range(len(arr)):
    sumA+=arr[i]
    if(sumA>maxA):
        maxA=sumA
    if(sumA<0):
        sumA=0

print(maxA)
        