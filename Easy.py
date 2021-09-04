# --------------------------------------------------Q1) Reverse integer------------------------------------------
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# cases = 1032, Runtime: 16 ms ,Memory Usage: 13.4 MB

# import math
# x = int(input())
# low = int(math.pow(-2,31))
# high = int(math.pow(2,31)-1)
# if x==0:
#     print(0)
# else:
#     final= ''
#     o = x
#     if x<0:
#         x = x*-1
#     while(x!=0):
#         r = x%10
#         x = int(x/10)
#         final += str(r)
#     if o>0:
#         s = int(final)
#         if (s > high or s == high):
#             print(0)
#         else:
#             print(s)
#     else:
#         f = int('-'+final)
#         if (f < low or f == low):
#             print(0)
#         else:
#             print(f)

# ---------------------------------------------Q2) Palindrome----------------------------------------------------
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# cases = 11510, Runtime: 80 ms, Memory Usage: 13.3 MB

# x = int(input())
# ori = x
# rev=0
# if x<0:
#     print(False)
# else:
#     while x!=0:
#         y = int(x%10)
#         rev = (rev*10) + y
#         x = int(x/10)
#     final = True if ori==rev else False
#     print(final)

# -----------------------------------------------Q3) Sum--------------------------------------------------------
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# cases = 55, Runtime: 7519 ms, Memory Usage: 13.9 MB

# nums = int(input(""))
# arr = []
# for i in range (0,nums):
#     ele= int(input())
#     arr.append(ele)

# print(arr)
# target = int(input('target: '))
# one=0
# second = 0
# for i in range (0, nums-1):
#     for j in range (0,nums-1):
#         if (arr[i]+arr[j] == target):
#             one = i
#             second = j
#             break

# ans = [second,one]
# print(ans)

# -------------------------------------------Q4) Remove Duplicates----------------------------------------------
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 

# cases = 362,Runtime: 60 ms,Memory Usage: 15.2 MB

# nums = [-1,-1,0,0]
# ori = len(nums)
# if (ori>0 ):
#     nums.append(-101)
# for i in range(0, ori):
#     if (nums[i] != nums[i+1]):
#         nums.append(nums[i])

# del nums[0:ori+1]
# print(nums)

# ------------------------------------------------Q5) Remove Element--------------------------------------------
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

#  cases: 113 , Runtime: 16 ms, Memory Usage: 13.2 MB

# nums = [2,2,2,2,5,3,6,8,3]
# val = 2
# i=0
# while i<len(nums):
#     if(nums[i] == val):
#         nums.pop(i)
#         i=0
#     else:
#         i +=1

# print(nums)

# ---------------------------------------------Q6) Sqrt(x)-------------------------------------------------------
# Given a non-negative integer x, compute and return the square root of x.only the integer part of the result is returned. Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# cases: 1017, Runtime: 20 ms, Memory Usage: 13.3 MB

import math
x = 4
y = math.sqrt(x)
print(int(y))
