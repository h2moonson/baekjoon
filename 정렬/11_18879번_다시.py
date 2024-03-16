# # @@@@@@@@@@시간 초과 
# N = int(input())
# initial_coord = list(map(int, input().split()))
# compressed_coord = []
# for i in range (N):
#     n_num = initial_coord[i]
#     filter = []
#     count = 0
#     for j in range (N):
#         if n_num > initial_coord[j] and initial_coord[j] not in filter:
#             filter.append(initial_coord[j])
#             count+=1
#     compressed_coord.append(count)
# print(*compressed_coord)


# @@@@@@@@@@더 빠른 알고리즘 O(NlogN)
N = int(input())
initial_coord = list(map(int, input().split()))
# 중복을 제거하고 정렬한 좌표 리스트 생성
# >> 이렇게 하면 인덱스 자체가 자기보다 작은 원소 개수임 
sorted_coord = sorted(list(set(initial_coord)))
compressed_coord = {}

# 중복을 제거한 정렬된 좌표 리스트의 각 좌표에 대해 압축된 값을 계산하여 딕셔너리에 저장
for i, coord in enumerate(sorted_coord):
    #print(i, coord)
    compressed_coord[coord] = i # 딕셔너리에 원소를 key값으로, value를 인덱스로 넘겨줘서 print문에 key값 넣으면 나오도록 
# 초기 좌표 리스트에 대해 압축된 값을 출력
for x in initial_coord:
    print(compressed_coord[x], end=' ')
print("")