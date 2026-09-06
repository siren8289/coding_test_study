#두 숫자가 같으면 good pair야.
# 단, 앞쪽 위치 i가 뒤쪽 위치 j보다 작아야 해.
# 이 입력의 정답은 4야


nums = [1, 2, 3, 1, 1, 3]
count=0 #조건에 맞는 쌍이 몇 개인지 세는 카운터 0부터 시작

for i in range(len(nums)):#모든 위치의 숫자를 하나씩 확인
    for j in range(i+1, len(nums)): #i 다음 위치부터 확인
        if nums[i]==nums[j]:
            count+=1 #조건에 맞는 쌍을 찾으면 카운트+1
print(count)


