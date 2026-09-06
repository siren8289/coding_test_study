def solution(n):
    total=0
    for i in range(1, 1+n):
        if i%2==0:
            total+=i
    return total
print(solution(10))