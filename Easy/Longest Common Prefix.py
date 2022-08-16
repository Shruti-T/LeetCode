# --------------------------------------- Q16)Longest Common Prefix -------------------------------------
# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# cases: 123, Runtime: 32 ms, Memory Usage: 13.5 MB

strs = ["a","ab"]
commonTwo = ""
if (len(strs) == 1):
    print(strs[0])
else:
    for i in range(0, len(strs[0])+1):
        if(strs[0][0:i] == strs[1][0:i]):
            commonTwo = strs[0][0:i]
    if(len(strs) >2):
        comLen = len(commonTwo)
        ori = commonTwo
        for k in range (2,len(strs)):
            if (strs[k] != ""):
                for j in range(1, comLen+1):
                    if(ori[0:j] == strs[k][0:j]):
                        commonTwo = ori[0:j]
                    elif(ori[0:1] != strs[k][0:1]):
                        commonTwo = ""
            else:
                commonTwo= ""
            ori = commonTwo
print(commonTwo)
