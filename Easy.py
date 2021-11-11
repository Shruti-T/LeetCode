# ---------------------------------------------Q1) Palindrome----------------------------------------------------
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

# -----------------------------------------------Q2) Sum--------------------------------------------------------
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

# -------------------------------------------Q3) Remove Duplicates----------------------------------------------
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

# ------------------------------------------------Q4) Remove Element--------------------------------------------
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

# ---------------------------------------------Q5)Sqrt(x)-------------------------------------------------------
# Given a non-negative integer x, compute and return the square root of x.only the integer part of the result is returned. Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# cases: 1017, Runtime: 20 ms, Memory Usage: 13.3 MB

# import math
# x = 4
# y = math.sqrt(x)
# print(int(y))


# ----------------------------------------------Q6) Binary add---------------------------------------------------
# Given two binary strings a and b, return their sum as a binary string.

# cases: 294, Runtime: 12 ms, Memory Usage: 13.6 MB

# a = "11"
# b = "1"
# sum = bin(int(a, 2) + int(b, 2))
# print(sum[2:])



# -----------------------------------------------Q7) Length of Last Word-----------------------------------------
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

# cases: 58, Runtime: 24 ms, Memory Usage: 13.8 MB

# import re
# s = "a uhwef fewjoij feff        "
# y = re.split("\s",re.sub(" +", " ", s))
# for i in range(0, len(y)):
#     if(y[i] != ''):
#         d = y[i]
# print(d)

# ------------------------------------------------Q8) Search Insert Position -----------------------------------
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

# cases: 62, Runtime: 28 ms, Memory Usage: 14.1 MB

# nums = [1,2,6,8]
# target = 7
# try:
#     x = nums.index(target)
# except:
#     nums.append(target)
#     nums.sort()
#     x = nums.index(target)

# print(x)

# -------------------------------------------------Q9) Plus One-------------------------------------------------
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# cases: 111, Runtime: 24 ms, Memory Usage: 13.3 MB

# digits = [4,3,2,1]
# num =""
# for i in range(0, len(digits)):
#     num += str(digits[i])

# final = int(num)+1
# x = [int(a) for a in str(final)]
# print(x)


# ------------------------------------------------Q10) Majority Element------------------------------------------
# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# cases: 47, Runtime: 120 ms, Memory Usage: 14.6 MB

# nums = [1,2,1,2,1,2,2,2,2,3]
# unique = list(dict.fromkeys(nums))
# for i in unique:

#     if(nums.count(i) > len(nums)/2):
#         x = i
#         break

# print(x)

# --------------------------------------------Q11) Single one-------------------------------------------------
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

# cases: 61, Runtime: 108 ms, Memory Usage: 15.8 MB

# nums = [9,1,2,3,1,2,3,4,0,4,0]
# nums.sort()
# nums.append(-4 * 10000)
# for i in range(0,len(nums)):
#     if(i%2 == 0 or i==0):
#         if(nums[i] != nums[i+1]):
#             x = nums[i]
#             break
# print(x)

# ----------------------------------------- Q12)Valid Palindrome -------------------------------------------
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

# cases: 480, Runtime: 28 ms, Memory Usage: 15.6 MB

# import re
# s = "ab_a"
# s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
# back=s[len(s)::-1]
# if(back == s):
#     print('true')
# else:
#     print('false') 

# ---------------------------------------Q13)Merge Sorted Array --------------------------------------------
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# cases: 59, Runtime: 16 ms, Memory Usage: 13.2 MB

# nums1 = [2]
# nums2 = []
# m = 1
# n = 0
# del nums1[len(nums1)-n:len(nums1)]
# nums1.extend(nums2)
# nums1.sort()
# print(nums1)

# ------------------------------------------- Q14)Roman to Integer ---------------------------------------------
# Given a roman numeral, convert it to an integer.

# cases: 3999, Runtime: 48 ms, Memory Usage: 13.7 MB

def split(s):
    return [char for char in s]

s = "IX"
arr = split(s)

for i in range(0,len(arr)):
    if(arr[i] == 'X'):
        arr[i] = 10
    elif(arr[i] == 'I'):
        arr[i] = 1
    elif(arr[i] == 'V'):
        arr[i] = 5
    elif(arr[i] == 'L'):
        arr[i] = 50
    elif(arr[i] == 'C'):
        arr[i] = 100
    elif(arr[i] == 'D'):
        arr[i] = 500
    elif(arr[i] == 'M'):
        arr[i] = 1000

solArr = []
extra = []
for i in range(0,len(arr)):
    if(i<len(arr)-1):
        if(arr[i]<arr[i+1]):
            ele = arr[i+1] - arr[i]
            solArr.append(ele)
            extra.append(arr[i+1])
        else:
            solArr.append(arr[i])
    else:
        solArr.append(arr[i])

for i in extra:
    solArr.remove(i)

sol = 0
for i in solArr:
    sol += i

print(sol)
