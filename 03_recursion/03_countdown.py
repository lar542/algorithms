def countdown(i):
    print(i)
    if i <= 1: # 기본단계
        return
    else:   # 재귀단계
        countdown(i-1)

def main():
    countdown(10)

if __name__ == "__main__":
    main()
