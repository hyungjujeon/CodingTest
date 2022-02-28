def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for person in room:
            answer[person - 1] += 1
        answer[l - 1] += len(room)

    return answer

def main():
    input_list = [[[1,4,2,3],[2,1,3,4]], [[3,2,1],[2,1,3]], [[3,2,1],[1,3,2]], [[1,4,2,3],[2,1,4,3]]]
    result = [[0,1,1], [2,2,1,3], [1,1,2], [2,2,2], [2,2,0,2]]
    for input in input_list:
        print(solution(input[0], input[1]))