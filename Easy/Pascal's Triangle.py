# ------------------------------------ Q15) Pascal's Triangle -----------------------------------------------
# Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# cases: 14, Runtime: 24 ms, Memory Usage: 13.4 MB

def fact(num):
    sol = 1 if (num==1 or num==0) else num * fact(num - 1)
    return sol

def pascalArr(row):
    solArr = []
    for i in range(0,row):
        newArr =[]
        for j in range(0,i+1):
            ele = int(fact(i)/(fact(i-j)*fact(j)))
            newArr.append(ele)
        solArr.append(newArr)
    return solArr


numRows = 30
val = pascalArr(numRows)
print(val)

