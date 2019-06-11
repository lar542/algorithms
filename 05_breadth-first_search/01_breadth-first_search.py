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