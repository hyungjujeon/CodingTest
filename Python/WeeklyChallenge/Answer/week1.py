def solution(price, money, count):
    fee = price * count * (count + 1) / 2
    answer = 0 if money > fee else fee-money
    return answer

def main():
    price = 3
    money = 20
    count = 4

    print(solution(price, money, count))