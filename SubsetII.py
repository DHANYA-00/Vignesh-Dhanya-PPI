def SubsetII(nums):
    for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
    sol = []

    def backtrack(index,res):
        sol.append(res[:])
            

        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            backtrack(i+1,res+[nums[i]])
    backtrack(0,[])
    return sol
nums = list(map(int,input().split()))
print(SubsetII(nums))
