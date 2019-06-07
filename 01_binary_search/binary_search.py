# list 정렬된 리스트
# item 찾으려는 요소 값
# return 찾으려는 요소의 위치
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        mid = (low + high) // 2 #중간 위치
        guess = list[mid]

        if guess == item :
            print(item,"은",mid,"위치에 있습니다")
            break
        if guess < item :
            print("추측한 숫자가 작습니다", "위치 =", mid)
            low = mid + 1
        else :
            print("추측한 숫자가 큽니다", "위치 =", mid)
            high = mid - 1

def main():
    binary_search([1,2,3,4,5,6,7,8,9,10], 3)

if __name__ == "__main__":
    main()
