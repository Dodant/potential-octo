N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []

min_count = abs(N-100)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken: break
        elif j == len(nums)-1:
            min_count = min(min_count, abs(N-int(nums))+len(nums))
        
print(min_count)