nums=[1,1,2,2]


sit={}

for num in nums:
    sit[num]=None

nums[:]=list(sit.keys())


print(nums)