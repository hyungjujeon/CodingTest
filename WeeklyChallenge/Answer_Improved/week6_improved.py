def solution(weights, head2head):
    WEIGHT = 0
    WIN_RATE = 1
    WIN_OVERWEIGHT_COUNT = 2

    boxer_info_dict = {num: [weight] for num, weight in enumerate(weights)}

    for i in range(len(head2head)):
        record = list(head2head[i])

        win_count = 0
        lose_count = 0
        win_overweight_count = 0

        for j in range(len(head2head)):
            if head2head[i][j] == 'W':
                win_count += 1

                my_weight = boxer_info_dict[i][WEIGHT]
                your_weight = boxer_info_dict[j][WEIGHT]

                if my_weight < your_weight:
                    win_overweight_count += 1

            elif head2head[i][j] == 'L':
                lose_count += 1

        try:
            boxer_info_dict[i].append((win_count / (win_count + lose_count)))
        except:
            boxer_info_dict[i].append(0)

        boxer_info_dict[i].append(win_overweight_count)

    answer = [num[0]+1 for num in sorted(boxer_info_dict.items(), key=lambda x:(x[1][WIN_RATE], x[1][WIN_OVERWEIGHT_COUNT], x[1][WEIGHT], -x[0]), reverse=True)]

    return answer

def main():
    input_list = [[[50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]], [[145, 92, 86], ["NLW", "WNL", "LWN"]], [[60, 70, 60], ["NNN", "NNN", "NNN"]]]
    for input in input_list:
        solution(input[0], input[1])