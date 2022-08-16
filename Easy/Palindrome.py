# ---------------------------------------------Q1) Palindrome----------------------------------------------------
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# cases = 11510, Runtime: 80 ms, Memory Usage: 13.3 MB

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
