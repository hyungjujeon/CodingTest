def solution(weights, head2head):
    WEIGHT = 0
    WIN_COUNT = 1
    WIN_COUNT_OW = 2

    boxer_info_dict = {num: [weight] for num, weight in enumerate(weights)}

    for i, record in enumerate(head2head):
        record = list(record)
        win_count = record.count('W')
        lose_count = record.count('L')
        if win_count + lose_count != 0:
            boxer_info_dict[i].append(win_count/(win_count + lose_count))
        else:
            boxer_info_dict[i].append(0)

        search_idx = 0
        win_count_overweight = 0
        for _ in range(win_count):
            opponent_idx = search_idx + record[search_idx:].index('W')
            my_weight = boxer_info_dict[i][WEIGHT]
            your_weight = boxer_info_dict[opponent_idx][WEIGHT]
            if my_weight < your_weight:
                win_count_overweight += 1
            search_idx = opponent_idx + 1
        boxer_info_dict[i].append(win_count_overweight)

    answer = [num[0]+1 for num in sorted(boxer_info_dict.items(), key=lambda x:(x[1][WIN_COUNT], x[1][WIN_COUNT_OW], x[1][WEIGHT], -x[0]), reverse=True)]

    return answer

def main():
    input_list = [[[50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]], [[145, 92, 86], ["NLW", "WNL", "LWN"]], [[60, 70, 60], ["NNN", "NNN", "NNN"]]]
    for input in input_list:
        solution(input[0], input[1])