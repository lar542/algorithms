알고리즘 개념 정리
=========

# 1. 이진탐색
* **오름차순으로 정렬된 리스트**에서 특정 값의 위치를 찾기 위해 처음부터 찾기 시작하는 것이 아니라 **중간**에서 찾기 시작하는 것
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
![선택 정렬 애니메이션](/02_selection_sort/Selection-Sort-Animation.gif)
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
-------------------------------------------------------
# 4. 퀵 정렬
## 4.1. 분할 정복
* 문제 해결 방법 중에서 가장 유명한 재귀적 알고리즘
* 문제를 풀기 위한 방법론에 가깝다.

분할 정복 전략은 다음과 같이 동작한다.
1. 기본 단계를 찾는다.
2. 주어진 문제를 작게 줄여서 기본 단계가 되도록 만드는 법을 찾는다.

### 4.1.1. 배열의 합계 구하기
#### 반복문으로 합계 구하기
```python
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def main():
    print(sum([1,2,3,4,5]))

if __name__ == "__main__":
    main()
```
#### 재귀 함수로 합계 구하기
1. 기본단계 : 원소의 개수가 0이면 합계는 0
2. 재귀단계 : 기본단계가 될 때까지 대상이 되는 배열의 크기를 줄여서 보낸다.
```python
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

def main():
    print(sum([1,2,3,4,5]))

if __name__ == "__main__":
    main()
```

## 4.2. 퀵 정렬
* 선택 정렬보다 훨씬 빠른 정렬 알고리즘
* 분할 정복 전략

1. 기본단계 : 원소의 개수가 0이거나 1
2. 기준원소 : 배열에서 원소하나를 고른다.
3. 분할 : 모든 원소를 기준원소보다 작은 숫자로 이루어진 배열, 기준원소보다 큰 숫자들로 이루어진 배열로 나눈다.
4. 두 개의 하위 배열에 대해 재귀적으로 퀵 정렬을 호출하고 그 결과를 합치면 전체 배열이 정렬된다.
```python
def quicksort(array):
    if len(array) < 2:
        return array # 기본단계
    else:
        pivot = array[0] # 기준원소
        # 분할
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    print(quicksort([3,5,2,1,4]))

if __name__ == "__main__":
    main()
```
-------------------------------------------------------
# 5. 너비 우선 탐색
* A에서 B로 가는 경로가 있는지 알려준다.
* 만약 경로가 존재한다면 최단 경로도 찾아준다.
* X까지의 최단 경로를 찾는 문제가 있다면
    1. 문제를 그래프로 모형화한다.
    2. 너비 우선 탐색으로 문제를 푼다.

## 5.1. 망고 판매상 찾기
친구 중에서 망고 판매상을 찾는다. 친구 중에 망고 판매상이 없다면 그 친구의 친구를 찾아본다. 또 그 중에서 없다면 친구의 친구의 친구 중에서 찾아본다. 망고 판매상에 도달할 때까지 전체 네트워크를 탐색한다.  
이를 너비 우선 탐색 알고리즘으로 나타낼 수 있다.
1. 네트워크에 망고 판매상이 있는가? → 그래프로 모형화하기 위해 관계를 표시하는 자료구조인 **해시 테이블**을 사용한다.
    * 해시 테이블은 순서를 가지지 않기 때문에 어떤 순서로 목록에 추가해도 상관없다.
2. 누가 가장 가까운 망고 판매상인가? → 목록에 추가한 순서대로 탐색해야 하므로 **큐**를 사용한다.
    * 큐 : 선입선출 자료구조(FIFO, First In First Out)
```python
from collections import deque

# 이름이 m으로 끝나면 망고 판매상으로 판단한다.
def person_is_seller(name):
    return name[-1] == 'm'

# 그래프로 모형화 : 관계를 표시하는 자료구조인 해시 테이블 사용
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque() # 탐색을 위한 큐 생성
    search_queue += graph[name] # 탐색할 사람을 큐에 추가
    searched = [] # 이미 확인한 사람의 명단

    # 큐가 비어있지 않는 한 계속 반복
    while search_queue:
        person = search_queue.popleft() # 큐의 첫번째 요소를 꺼냄
        if not person in searched:
            if person_is_seller(person):
                print(person + "는 망고 판매상이다!")
                return True
            else:
                search_queue += graph[person] # 망고 판매상이 아닐 때 그의 이웃을 다시 큐에 추가
                searched.append(person)
    return False

search("you")
```