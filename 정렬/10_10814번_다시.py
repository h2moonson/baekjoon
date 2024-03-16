N = int(input())
age_name = [input().split() for _ in range (N)]
for i in range(N) : 
    age_name[i].append(i) #최초의 인덱스를 넣자
#print(age_name)

age_name.sort(key = lambda x: (int(x[0]), int(x[2]))) #나이나 인덱스를 문자열로 저장하면 "10"이 "2"보다 앞에옴


sorted_members = sorted(age_name, key=lambda x: (int(x[0]), age_name.index(x)))
# index쓰면 선형 시간복잡도를 갖기에 너무 오래걸림 >>!!! 


#print(age_name)
for member in age_name:
    print(member[0], member[1])