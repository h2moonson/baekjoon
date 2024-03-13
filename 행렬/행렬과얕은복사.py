# https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
# 1차원 배열 선언 
rows= 10 
arr = [0] * rows 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 같은 방식으로 2차원 배열 선언 시 문제점 
rows = 10
cols = 5
arr = [[0] * cols] * rows

arr[0][0] = 1 # 이렇게 할 경우 arr 행의 모든 0열의 값이 1로 변경이 된다
[[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]

#그 이유는 *를 선언해서 배열 선언 시 얕은 복사가 일어남 = 배열 내의 요소들이 같은 객체 가리킴

#mutable한 객체와 immutable한 객체 
a = [1, 2, 3]
id(a)
4393788808
a[0] = 5
a
[5, 2, 3]
id(a)
4393788808 # 값을 변경해도 메모리의 주소값 그대로임 


#str의 경우는 immutable한 객체. 
s= "abc"
s
'abc'
id(s)
4387454680
s[0]
'a'
s[0] = 's'
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'str' object does not support item assignment 

#immutable한 객체는 변경이 안됨
s = 'def'
s
'def'
id(s)
4388970768  #재할당을 할 경우 아예 id가 변경되는 것을 확인할 수 있음 

# https://wikidocs.net/16038

import copy
b = copy.deepcopy(a)  
#mutable객체 안에 mutable객체가 있는 다차원배열의 경우
#slicing으로 shallowcopy해도 그 안에 내부 원소 
# id(a)와 id(b)는 다르지만 id(a[0])은 id(b[0])과 같게 됨. 이를 해결
