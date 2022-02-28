def solution(scores):
    new_scores = list(map(list, zip(*scores)))
    answer = ''
    for i, scores_for_i in enumerate(new_scores):
        average = 0
        if max(scores_for_i) == scores_for_i[i] and scores_for_i.count(scores_for_i[i]) == 1:
            average = (sum(scores_for_i) - scores_for_i[i]) / (len(scores_for_i) - 1)
        elif min(scores_for_i) == scores_for_i[i] and scores_for_i.count(scores_for_i[i]) == 1:
            average = (sum(scores_for_i) - scores_for_i[i]) / (len(scores_for_i) - 1)
        else:
            average = sum(scores_for_i) / len(scores_for_i)

        if average >= 90:
            answer += 'A'
        elif average >= 80:
            answer += 'B'
        elif average >= 70:
            answer += 'C'
        elif average >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

def main():
    scores_ex1 = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                  [24, 90, 94, 75, 65]]
    scores_ex2 = [[50, 90], [50, 87]]
    scores_ex3 = [[70, 49, 90], [68, 50, 38], [73, 31, 100]]

    print(solution(scores_ex1))
    print(solution(scores_ex2))
    print(solution(scores_ex3))