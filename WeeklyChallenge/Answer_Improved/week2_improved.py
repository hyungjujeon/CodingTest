def solution(scores):
    new_scores = [[i[j] for i in scores] for j in range(len(scores))]
    average_list = []
    for i, scores_for_i in enumerate(new_scores):
        average = 0
        if (max(scores_for_i) == scores_for_i[i] or min(scores_for_i) == scores_for_i[i]) and scores_for_i.count(scores_for_i[i]) == 1:
            average = (sum(scores_for_i) - scores_for_i[i]) / (len(scores_for_i) - 1)
        else:
            average = sum(scores_for_i) / len(scores_for_i)
        average_list.append(average)

    answer = "".join([ (avg>=90 and "A") or (avg>=80 and "B") or (avg>=70 and "C") or (avg>=50 and "D") or "F" for avg in average_list])
    return answer

def main():
    scores_ex1 = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                  [24, 90, 94, 75, 65]]
    scores_ex2 = [[50, 90], [50, 87]]
    scores_ex3 = [[70, 49, 90], [68, 50, 38], [73, 31, 100]]

    print(solution(scores_ex1))
    print(solution(scores_ex2))
    print(solution(scores_ex3))