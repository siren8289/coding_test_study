# #첫 번째 → 1
# 두 번째 → 1 + 2 = 3
# 세 번째 → 1 + 2 + 3 = 6
# 네 번째 → 1 + 2 + 3 + 4 = 10

nums = [1, 2, 3, 4]
total=0
result=[]

for i in nums:
    total+=i
    result.append(total)

    print(result)
