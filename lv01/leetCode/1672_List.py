#for문으로 한사람씩 꺼내려면?
#이제 해야 할 건 각 person의 숫자를 전부 더해서
#그 사람의 총액을 구하는 것이야

accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
totals=[] #빈 리스트 만듦 | 빈 바구나 먼저 만듦

for person in accounts: #한 사람의 계좌목록 들어옴
    total=sum(person) #각 사람의 총액
    totals.append(total) #total을 totals에 추가
print(max(totals)) #가장 큰 값을 구하기