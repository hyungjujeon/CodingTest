def solution(word):
    answer = 0
    for i, char in enumerate(word):
        coef = ((5 ** (5 - i) - 1) / (5 - 1))
        answer += coef * "AEIOU".index(char) + 1
    return answer

def main():
    word_list = ['AAAAE', 'AAAE', 'I', 'EIO']
    for word in word_list:
        print('답', solution(word))
        print("#######################")