# -------------------------Reverse integer--------------------------
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

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

# ---------------------------------Palindrome-----------------------------------------
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


x = int(input())
ori = x
rev=0
if x<0:
    print(False)
else:
    while x!=0:
        y = int(x%10)
        rev = (rev*10) + y
        x = int(x/10)
    final = True if ori==rev else False
    print(final)