# BOOKMARK <#1> : [LIST] 간단한 6가지 리스트 생성법
class MakeSimpleList:
    def __init__(self):
        self.my_list = None

    def msl_1(self):
        self.my_list = [1, 2, 3]

        return self.my_list

    def msl_2(self):
        self.my_list = list()
        self.my_list.append(1)
        self.my_list.append(2)
        self.my_list.append(3)

        return self.my_list

    def msl_3(self):
        self.my_list = []
        self.my_list.append(1)
        self.my_list.append(2)
        self.my_list.append(3)

        return self.my_list

    def msl_4(self):
        self.my_list = list(range(1, 4))

        return self.my_list

    def msl_5(self):
        self.my_list = [i for i in range(1, 4)]

        return self.my_list

    def msl_6(self):
        self.my_list = [0] * 3

        return self.my_list


# BOOKMARK <#2> : [LIST] range, enumerate 를 이용한 반복문
class ListIteration:
    def __init__(self):
        self.my_list = None

    def li_1(self):
        self.my_list = []
        for i in range(5):
            self.my_list.append(i+1)

        return self.my_list
        # [1, 2, 3, 4, 5]

    def li_2(self):
        num_list = [1, 2, 3, 4, 5]
        for t in enumerate(num_list):
            self.my_list.append(t)

        return self.my_list
        # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

    def li_3(self):
        num_list = [1, 2, 3, 4, 5]
        for i, v in enumerate(num_list):
            self.my_list.append(v)

        return self.my_list
        # [1, 2, 3, 4, 5]

    # BOOKMARK <#2-1> : [LIST] 반복문 실행 시 제어자는 고정이다.
    # def li_4_caution(self):
    #     num_list = list(range(1,6))
    #     for i in range(len(num_list)):
    #         print(f'index : {i}, length : {len(num_list)}')
    #         if num_list[i] >= 4:
    #             num_list.pop(i)
    #
    #     # num_list 길이가 반복문 수행중 변하더라도, 반복문은 0부터 4번째 index 까지 순서대로 가기로 되어있다. (제어자는 고정)
    #     # 따라서, num_list = [1, 2, 3, 5]가 된 후 index 4는 존재하지 않으므로 IndexError 가 발생하게 되므로 조심
