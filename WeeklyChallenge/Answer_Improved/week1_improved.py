def solution(price, money, count):
    fee = price * count * (count + 1) / 2
    answer = 0 if money > fee else fee-money
    return answer

def solution_improved1(price, money, count):
    return max(0, price * count * (count + 1) // 2 - money)

def solution_improved2(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))

def main():
    price = 3
    money = 20
    count = 4

    print(solution(price, money, count))