numbers = [1, 2, 1, 3, 1, 2]
count={}
for num in numbers:
    # if num in numbers:
    #     count[num]+=1
    # else:
    #     count[num]=1

    count[num]=count.get(num,0)+1

print(count)