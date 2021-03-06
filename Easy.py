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
# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ???n / 2??? times. You may assume that the majority element always exists in the array.

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

# def split(s):
#     return [char for char in s]
# s = "IX"
# arr = split(s)

# for i in range(0,len(arr)):
#     if(arr[i] == 'X'):
#         arr[i] = 10
#     elif(arr[i] == 'I'):
#         arr[i] = 1
#     elif(arr[i] == 'V'):
#         arr[i] = 5
#     elif(arr[i] == 'L'):
#         arr[i] = 50
#     elif(arr[i] == 'C'):
#         arr[i] = 100
#     elif(arr[i] == 'D'):
#         arr[i] = 500
#     elif(arr[i] == 'M'):
#         arr[i] = 1000

# solArr = []
# extra = []
# for i in range(0,len(arr)):
#     if(i<len(arr)-1):
#         if(arr[i]<arr[i+1]):
#             ele = arr[i+1] - arr[i]
#             solArr.append(ele)
#             extra.append(arr[i+1])
#         else:
#             solArr.append(arr[i])
#     else:
#         solArr.append(arr[i])

# for i in extra:
#     solArr.remove(i)

# sol = 0
# for i in solArr:
#     sol += i
# print(sol)

# ------------------------------------ Q15) Pascal's Triangle -----------------------------------------------
# Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# cases: 14, Runtime: 24 ms, Memory Usage: 13.4 MB

# def fact(num):
#     sol = 1 if (num==1 or num==0) else num * fact(num - 1)
#     return sol

# def pascalArr(row):
#     solArr = []
#     for i in range(0,row):
#         newArr =[]
#         for j in range(0,i+1):
#             ele = int(fact(i)/(fact(i-j)*fact(j)))
#             newArr.append(ele)
#         solArr.append(newArr)
#     return solArr


# numRows = 30
# val = pascalArr(numRows)
# print(val)


# --------------------------------------- Q16)Longest Common Prefix -------------------------------------
# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# cases: 123, Runtime: 32 ms, Memory Usage: 13.5 MB

# strs = ["a","ab"]
# commonTwo = ""
# if (len(strs) == 1):
#     print(strs[0])
# else:
#     for i in range(0, len(strs[0])+1):
#         if(strs[0][0:i] == strs[1][0:i]):
#             commonTwo = strs[0][0:i]
#     if(len(strs) >2):
#         comLen = len(commonTwo)
#         ori = commonTwo
#         for k in range (2,len(strs)):
#             if (strs[k] != ""):
#                 for j in range(1, comLen+1):
#                     if(ori[0:j] == strs[k][0:j]):
#                         commonTwo = ori[0:j]
#                     elif(ori[0:1] != strs[k][0:1]):
#                         commonTwo = ""
#             else:
#                 commonTwo= ""
#             ori = commonTwo
# print(commonTwo)


# ------------------------------------------- Q17)Min Stack ------------------------------------------------
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class: MinStack() initializes the stack object. void push(int val). void pop(). int top(). int getMin().

#  cases: 33, Runtime: 56 ms, Memory Usage: 17MB

# class MinStack(object):
#    min=float('inf')
#    def __init__(self):
#       self.min=float('inf')
#       self.stack = []
#    def push(self, x):
#       if x<=self.min:
#          self.stack.append(self.min)
#          self.min = x
#       self.stack.append(x)
#    def pop(self):
#       t = self.stack[-1]
#       self.stack.pop()
#       if self.min == t:
#          self.min = self.stack[-1]
#          self.stack.pop()
#    def top(self):
#       return self.stack[-1]
#    def getMin(self):
#       return self.min

# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# param_4 = obj.getMin()
# print(param_4)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3, param_4)


# ----------------------------------- Q18) Two Sum II - Input Array Is Sorted -------------------------------
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2].Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# cases: 19, Runtime: 287 ms, Memory Usage: 13.4MB

# numbers = [-1,0]
# target = -1
# unique = list(set(numbers))
# for i in range (0,len(unique)):
#     for j in range (0, len(unique)):
#         if(j!=i):
#             if(unique[i] + unique[j] == target):
#                 x  = [unique[i], unique[j]]
#                 y = [numbers.index(x[0]) + 1, numbers.index(x[1]) + 1]
#                 break
#             elif(unique[i] + unique[i] == target and numbers.count(unique[i]) == 2):
#                 y = [numbers.index(unique[i]) + 1, numbers.index(unique[i]) + 2]
#                 break
# y.sort()
# print(y)

# ---------------------------------------- Q19) Remove Duplicates from Sorted List----------------------------
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#  cases: 166, Runtime: 166 ms, Memory Usage: 13.7 MB

# ----------(leetcode working solution)-------------
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         node = head
#         while node:
#             current = node
#             while current.next:
#                 if current.next.val == node.val:
#                     current.next = current.next.next
#                 else:current = current.next
#             node = node.next
#         return head

# ---------(my solution, not going with leetcode)-------------------
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def clearDuplicates(self):
#         arr = []
#         temp = self.head
#         while(temp):
#             if(temp.next == None):
#                 # print(temp.data)
#                 arr.append(temp.data)
#                 temp = temp.next
#             elif(temp.data == temp.next.data):
#                     # print(temp.data)
#                     arr.append(temp.data)
#                     temp=temp.next.next
#             else:
#                 temp = temp.next
#         return arr
#     def printLlist(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp=temp.next

# def pointerEle(old):
#     if(x==1):
#         llist2.head.next = ele
#     else:
#         old.next = ele

# llist = LinkedList()
# llist.head = Node(1)
# second = Node(1)
# third = Node(3)
# four = Node(3)
# fifth = Node(6)
# llist.head.next = second
# second.next = third
# third.next = four
# four.next = fifth
# # -------------
# array = llist.clearDuplicates()
# # print(array)
# llist2 = LinkedList()
# x = 0
# old = llist2
# for j in range(0,len(array)):
#     if(llist2.head == None):
#         llist2.head = Node(array[j])
#         x=1
#     else:
#         ele = Node(array[j])
#         pointerEle(old)
#         old = ele
#         x=0

# llist2.printLlist()
# print(llist2.head)                        

# ---------------------------------------------------- Q20) --------

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printLlist(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp=temp.next
    def merge(self, l1,l2):
        # self.head = l1
        # print(l1.next.val, l2.next.val)
        while(l1):
            print(l1.val,'dddd')
            while(l2):
                # print(l2.val,'ssss')
                if(l2.val <l1.val and l1 == l1.head):
                    # print('dd')
                    x = Node(l2.val)
                    x.next = l1.head
                    l1.head = x
                    l2.head = l2.next
                    
                elif(l2.val>l1.val and l1.next == None):
                    print('xx')
                    l1.next = l2
                    
                elif(l1.val<=l2.val or l2.val<=l1.next.val):
                    # print(l1.val,l1.next.val,l2.val)
                    y = Node(l2.val)
                    print(l2.val, l1.next.val)
                    y.next = l1.next
                    l1.next = y 
                    # l1 = l1.next
                l2 = l2.next
            l1=l1.next
           
        # l1.printLlist()
        # return l2

            
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(4)
llist.head.next = second
second.next = third

llist2 = LinkedList()
llist2.head = Node(1)
sec = Node(3)
thi = Node(4)
llist2.head.next = sec
sec.next = thi
# llist.printLlist()
print('-----')
# llist2.printLlist()
# l3 = LinkedList()
print('--aa----')
l3 = LinkedList()
l3.merge(llist.head, llist2.head)
print('yahuuuuu')
llist.printLlist()