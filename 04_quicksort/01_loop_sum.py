def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def main():
    print(sum([1,2,3,4,5]))

if __name__ == "__main__":
    main()