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