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