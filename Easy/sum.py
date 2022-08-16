
# -----------------------------------------------Q2) Sum--------------------------------------------------------
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# cases = 55, Runtime: 7519 ms, Memory Usage: 13.9 MB

nums = int(input(""))
arr = []
for i in range (0,nums):
    ele= int(input())
    arr.append(ele)

print(arr)
target = int(input('target: '))
one=0
second = 0
for i in range (0, nums-1):
    for j in range (0,nums-1):
        if (arr[i]+arr[j] == target):
            one = i
            second = j
            break

ans = [second,one]
print(ans)
