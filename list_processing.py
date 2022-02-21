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
