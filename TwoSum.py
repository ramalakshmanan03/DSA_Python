nums =[2,7,11,15]

target = 9

def twoSum():
   list = []
   for x in range(len(nums)):
      for y in range(len(nums)):
          if x == y:
            continue
          elif nums[x] + nums[y] == target:
                list.append(x)
                list.append(y)
                return list
   return []

print(twoSum())