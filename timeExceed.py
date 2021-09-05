# TO TRY AGAIN
# ---------------------------------------------Q7) Single one----------------------------------------------------

# nums = [1,1,2,8,8,2,0,9,0]
# for i in range(0, len(nums)):
#     iList = nums[:i] + nums[i+1:]
#     if (any(ele == nums[i] for ele in iList)):
#         nums.pop(i)
#         continue
#     else:
#         y = nums[i]
#         break        
# print(y)
# ------------------------------------------------------

# nums = [1,1,4,2,4,2,7,9,7,9,0]
# i=0
# x = None
# while i<len(nums):
#     if(nums.count(nums[i]) == 1):
#          x = nums[i]
#          break
#         # nums = list(filter(lambda x: x != nums[i], nums))   
#     else:
#         nums = list(filter(lambda x: x != nums[i], nums))   
#         # x = nums[i]
#         # break
# print(x)