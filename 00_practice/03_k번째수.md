# K번째수
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## 입출력 예
array  
[1, 5, 2, 6, 3, 7, 4]  
commands  
[[2, 5, 3], [4, 4, 1], [1, 7, 3]]  
return  
[5, 6, 3]  

## 입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.  
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.  
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

## 나의 풀이
```python
def solution(array, commands):
    answer = []
    for i in commands:
        aList = array[i[0]-1:i[1]]
        aList.sort()
        answer.append(aList[i[2]-1])
    return answer
```

## 다른 사람의 풀이1
* sorted : 주어진 값을 정렬 후 그 결과를 리스트로 리턴하는 파이썬 내장함수
* 리스트 내장함수인 sort 함수 : 리스트 객체 그 자체만 정렬할 뿐 그 결과를 리턴하지 않는다.
```python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command # 먼저 변수로 대입하기 때문에 읽기 쉽다.
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
```

## 다른 사람의 풀이2
```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```