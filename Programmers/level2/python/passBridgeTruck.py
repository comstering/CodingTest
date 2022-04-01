from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weight_queue = deque(truck_weights)    # 트럭 무게 큐
    bridge_queue = deque([0] * bridge_length)    # 다리 상태 큐
    bridge_weight = 0    # 다리를 건너는 중인 트럭의 총 무게
    answer = 0
    while truck_weight_queue or len(set(bridge_queue)) != 1:
        bridge_weight -= bridge_queue.popleft()    # 트럭이 다리를 다 건넜을 경우
        bridge_queue.append(0)
        answer += 1
        if truck_weight_queue:
            if bridge_weight + truck_weight_queue[0] <= weight:    # 다리가 트럭의 무게를 견딜 수 있을 경우
                truck_weight = truck_weight_queue.popleft()
                bridge_weight += truck_weight    # 다리를 건너는 중인 트럭무게에 트럭 무게 추가
                bridge_queue[-1] = truck_weight    # 다리 상태에 트럭 올리기
    return answer


print(solution(2, 10, [7, 4, 5, 6]))    # 8
print(solution(100, 100, [10]))    # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))    # 110
