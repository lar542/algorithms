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
