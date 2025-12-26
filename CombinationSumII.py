def CombinationSumII(candidates, target):
    n = len(candidates)
    for i in range(n):
        for j in range(n-i-1):
            if candidates[j] > candidates[j+1]:
                candidates[j],candidates[j+1] = candidates[j+1],candidates[j]
    sol = []
    res = []
    total = []
    def backtrack(index,res,total):
        if total == target:
            sol.append(res[:])
            return
            
        if total > target:
            return
            
        for i in range(index,n):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            backtrack(i+1,res+[candidates[i]],total+candidates[i])
        
    backtrack(0,[],0)
    return sol

candidates = list(map(int,input().split()))
target = int(input())
print(CombinationSumII(candidates,target))