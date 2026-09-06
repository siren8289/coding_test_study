#각 숫자의 자릿수가 짝수인 숫자가 몇 개인지 구해.
# #* Python: str(), len(), for, if
# * 자료구조: list, 문자열 str
# * 알고리즘: 순회 + 조건 검사 + 카운팅
# * 시간복잡도: 대략 O(n)으로 생각하고 시작
nums = [12, 345, 2, 6, 7896]
count=0 #조건에 맞는 쌍이 몇개인가?

for num in nums:
    len(str(num)) #str="345", len(str())="3"
    if num %2==0:
        count+=1
        print(num)