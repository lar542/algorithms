# 각 정점의 이웃과 가격을 그래프로 구현
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

'''
각 정점에 도달하는 가격(출발점에서 그 정점까지 걸리는 시간)을 저장
가격을 모르는 정점의 가격은 무한대로 둔다.
'''
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 각 정점까지 도달하는 데 거치는 부모를 저장
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 이미 처리한 정점을 저장
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # 아직 처리하지 않은 가장 싼 정점
# 모든 정점을 처리할 때까지 반복
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)