알고리즘 개념 정리
=========

# 1. 이진탐색
* __오름차순으로 정렬된 리스트__에서 특정 값의 위치를 찾기 위해 처음부터 찾기 시작하는 것이 아니라 __중간__에서 찾기 시작하는 것
* 정렬된 리스트에만 사용할 수 있다
* 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 실행시간이 대폭 감소된다 (최대 log n번 만에 찾을 수 있음)
```python
# list 오름차순 정렬된 리스트
# item : 찾으려는 요소 값
def binary_search(list, item):
    low = 0
    high = len(list) - 1
     
    while (low <= high):
        mid = (low + high) // 2 #중간 위치
        guess = list[mid]
         
        if guess == item :
            print(item,"은",mid,"인덱스에 있습니다")
            break
        if guess < item :
            print("추측한 숫자가 작습니다", "인덱스 =", mid)
            low = mid + 1
        else :
            print("추측한 숫자가 큽니다", "인덱스 =", mid)
            high = mid - 1
     
def main():
    binary_search([1,2,3,4,5,6,7,8,9,10], 3)
     
if __name__ == "__main__":
    main()
```
-------------------------------------------------------
# 2. 선택정렬
* O(n) 실행시간이 걸리는 연산을 n번 수행하는 것
* 주어진 리스트 중에 최소값을 찾아 맨 앞에 위치한 값과 교체하고 맨 앞의 값을 제외한 나머지를 같은 방법으로 교체하여 최종적으로 리스트를 정렬시킨다
* 메모리가 제한적인 경우에 사용시 성능 상의 이점이 있다
![선택 정렬 애니메이션]()
```python
# 배열에서 가장 작은 원소 값의 인덱스를 찾는다
def findSmallest(arr):
     smallest = arr[0] # 가장 작은 값
     smallest_index = 0 # 가장 작은 값의 인덱스
 
     for i in range(1, len(arr)):
       if arr[i] < smallest:
         smallest = arr[i]
         smallest_index = i
 
     return smallest_index
 
# 배열을 정렬한다
def selectionSort(arr):
    newArr = []
    # 가장 작은 원소 값을 찾아 새 배열에 추가하고 기존 배열의 원소 값은 삭제
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
 
    return newArr
 
def main():
    print("정렬결과 :", selectionSort([5, 3, 6, 2, 10]))
 
if __name__ == "__main__":
    main()
```
-------------------------------------------------------
# 3. 재귀
* 함수가 자기 자신을 호출하는 것
* 재귀 함수는 기본 단계와 재귀 단계로 나누어져 있다.
* 기본 단계 : 무한 반복으로 빠져들지 않게 하는 부분
* 재귀 단계 : 자기 자신을 호출하는 부분

## 3.1. 상자 안에서 열쇠를 찾는 코드를 의사코드로 나타내기
※ 의사코드 : 문제와 풀이 방법을 간단한 코드 형태로 설명한 것
* while 반복문을 사용한 경우
```python
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "열쇠를 찾았어요!"
```
* 재귀를 사용한 경우
```python
def look_for_key(box):
  for item in box:
      if item.is_a_box():
          look_for_key(item)
      elif item.is_a_key():
          print "열쇠를 찾았어요!"
```
## 3.2. 재귀를 사용해 팩토리얼 함수 구현하기
```python
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
 
def main():
    print(fact(5))
 
if __name__ == "__main__":
    main()
```
