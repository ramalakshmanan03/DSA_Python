nums =[2,7,11,15]
target = 9
mt ={}

def twosum(nums,target,mt):
    for x in range(len(nums)):
       sub = target - nums[x]
       if sub in mt:
             return [mt[sub],x]
       else:
                mt[nums[x]] = x
print(twosum(nums,target,mt))