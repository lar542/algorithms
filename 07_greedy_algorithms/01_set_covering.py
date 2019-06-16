# 방송하고자 하는 주의 목록
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

'''
방송국의 목록
Key : 방송국 이름, Value : 방송국이 방송하는 주의 목록
'''
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 방문한 방송국의 목록
final_stations = set()

while states_needed:
    best_station = None # 가장 많은 주를 방송하고 있는 방송국
    states_covered = set() # 해당 방송국이 방송하는 주의 집합
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 교집합
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations)