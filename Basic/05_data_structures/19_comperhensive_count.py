word=input()
count={}
for i in word:
    count[i]=count.get(i, 0)+1

for i, num in count.items():
    print(i, num)