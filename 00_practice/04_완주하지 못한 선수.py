def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = participant[len(participant)-1]
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            answer = participant[i]
            break
    return answer

def main():
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
    print(solution(["a", "b", "c", "d", "b", "d"], ['a', 'b', 'b', 'd', 'd']))

if __name__ == "__main__":
    main()