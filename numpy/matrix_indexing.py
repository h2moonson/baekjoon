import numpy as np
#특정 조건을 제시하면 그 조건에 해당하는 원소 또는 배열 자동으로 출력해줌

'''
numpy[array, column] 형식
numpy_array[행 인덱스 or 조건, 열 인덱스 or 조건]
: 왼쪽은 행 조건임. True인 행만 선택(두번째와 네번째 행만 선택)
: 오른쪽은 열 조건. 선택된 행에서 첫재~세번째 열 

[[ 4  5  6]
 [10 11 12]]
'''
# 예제1 : Boolean Indexing + Column Selection
A = np.array([1, 2, 3, 4])
A_even = (A % 2 == 0) #[False  True False  True]

sample = np.array([[1, 2, 3],
                  [ 4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])

print(sample[A_even, :3]) # [[ 4  5  6] [10 11 12]]

# 예제2 : 특정 행과 열 선택 
sample_2 = sample[[1, 3], [0, 2]] #1번, 3번 행 & 0번, 2번 열 선택

# 예제 3 : :를 활용한 전체 행 선택 
sample_3 = sample[:, 2]  # 모든 행에서 2번 열만 선택
print(sample_3)
