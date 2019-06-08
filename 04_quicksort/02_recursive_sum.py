def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

def main():
    print(sum([1,2,3,4,5]))

if __name__ == "__main__":
    main()