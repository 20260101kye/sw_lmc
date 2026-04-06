nums = []
for _ in range(10):
    n = int(input())
    r = n%42
    
    if r not in nums:
        nums.append(r)
print(len(nums))
    