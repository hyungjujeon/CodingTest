def calculate_diff(char):
    if char == 'A':
        return 0
    elif char == 'E':
        return 1
    elif char == 'I':
        return 2
    elif char == 'O':
        return 3
    elif char == 'U':
        return 4

def solution(word):
    char_diff_list = [] #[0] * 5
    digit_coefficient = [781, 156, 31, 6, 1]
    #word = word.ljust(5, 'X')
    for i, char in enumerate(word):
        char_diff_list.append(calculate_diff(char))
        print(char)
    print(char_diff_list)
    answer = len(word) + sum([char_diff_list[i] * digit_coefficient[i] for i in range(len(char_diff_list))])
        # 781 * (char_diff_list[0]) \
        #      + 156 * (char_diff_list[1]) \
        #      + 31 * (char_diff_list[2]) \
        #      + 6 * (char_diff_list[3]) \
        #      + 1 * (char_diff_list[4]) \
        #answer = 0
    return answer

def main():
    word_list = ['AAAAE', 'AAAE', 'I', 'EIO']
    #word_list = ['I']
    for word in word_list:
        print('답', solution(word))
        print("#######################")