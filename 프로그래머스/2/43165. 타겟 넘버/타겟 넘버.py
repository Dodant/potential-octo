def solution(numbers, target):
    idx = cur = 0
    
    def dfs(nums, target, cur, idx):
        if idx == len(nums):
            return 1 if cur == target else 0
        
        return dfs(nums, target, cur + nums[idx], idx + 1) \
            + dfs(nums, target, cur - nums[idx], idx + 1)

    answer = dfs(numbers, target, idx, cur)
    return answer