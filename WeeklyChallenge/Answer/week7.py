def solution(enter, leave):
    answer_dict = {person: 0 for person in enter}
    num_person = len(enter)

    for i in range(1, num_person + 1):
        for j in range(i + 1, num_person + 1):
            person1 = leave[-i]
            person2 = leave[-j]

            if enter.index(person1) < enter.index(person2):
                answer_dict[person1] += 1
                answer_dict[person2] += 1
            else:
                for k in range(max(i, j) + 1, num_person + 1):
                    threshold = max(enter.index(person1), enter.index(person2))
                    if threshold < enter.index(leave[-k]):
                        answer_dict[person1] += 1
                        answer_dict[person2] += 1
                        break

    return [num[1] for num in sorted(answer_dict.items(), key=lambda x: x[0])]

def main():
    input_list = [[[1,4,2,3],[2,1,3,4]], [[3,2,1],[2,1,3]], [[3,2,1],[1,3,2]], [[1,4,2,3],[2,1,4,3]]]
    result = [[0,1,1], [2,2,1,3], [1,1,2], [2,2,2], [2,2,0,2]]
    for input in input_list:
        print(solution(input[0], input[1]))