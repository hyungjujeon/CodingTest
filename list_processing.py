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


# BOOKMARK <#3> : [LIST] append, insert, extend, +(연산자)를 이용하여 추가하기
class ListInsertion:
    def __init__(self):
        self.my_list = [1, 2, 3]

    def refresh_list(self):
        self.my_list = [1, 2, 3]

    def li_append(self, value):
        self.refresh_list()
        self.my_list.append(value)  # 맨 마지막 index (-1) 에 value 가 들어감
        return self.my_list

    def li_insert(self, index, value):
        self.refresh_list()
        self.my_list.insert(index, value)  # 해당 index 에 value 가 들어감
        return self.my_list

    def li_extend(self):
        self.refresh_list()
        new_list = [4, 5]
        self.my_list.extend(new_list)  # my_list 에 new_list 가 이어 붙여짐
        return self.my_list

    def li_plus(self):
        self.refresh_list()
        new_list = [6, 7]
        self.my_list += new_list
        return self.my_list


# BOOKMARK <#4> : [LIST] pop, remove, del, slicing 을 이용하여 제거하기
class ListDeletion:
    # slicing 만 원래 list 에 영향을 받지 않고, 나머지 pop, remove, del 은 원래 list 에 영향을 줌(값 삭제)
    def __init__(self):
        self.my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def refresh_list(self):
        self.my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def ld_pop(self, index=None):
        self.refresh_list()
        if any(index):
            value = self.my_list.pop(index)  # list 에서 해당 index 값을 빼고 return 함
        else:
            value = self.my_list.pop()  # 맨 마지막 값(-1)을 list 에서 빼고 return 함

        return self.my_list

    def ld_remove(self, value):
        self.refresh_list()
        self.my_list.remove(value)  # list 에서 해당 value 에 해당되는 값을 빼고 return 은 하지 않음
        # 만약 여러개면, 0번에서 가까운 요소가 삭제된다.

        return self.my_list

    def ld_del_idx(self, index):
        self.refresh_list()
        del self.my_list[index]  # list 에서 해당 index 값을 빼고 return 은 하지 않음

        return self.my_list

    def ld_del_slicing(self, start, end, step):
        self.refresh_list()
        del self.my_list[start: end: step]  # start 부터 end-1 index 전 까지 step 만큼에 해당되는 값을 빼고 return 은 하지 않음

        return self.my_list

    def ld_slicing(self, start, end, step):
        self.refresh_list()
        self.my_list = self.my_list[start: end: step]  # 순수 slicing 은 list 에 영향 주지 않으므로 재정의 해야 함


# BOOKMARK <#5> : [LIST] slicing 이용하기 > list[start: end: step]
class ListSlicing:
    def __init__(self):
        # 양수 index  :   0  1  2  3  4  5  6  7  8  9
        self.num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 음수 index  :  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

    def ls_slicing_positive(self):
        result1 = self.num_list[:4]  # 처음부터 index 4 전까지(3) : [1, 2, 3, 4]
        result2 = self.num_list[3:]  # index 3 부터 마지막까지 : [4, 5, 6, 7, 8, 9, 10]
        result3 = self.num_list[::2]  # 처음을 시작으로 하나씩 건너 뛰면서 : [1, 3, 5, 7, 9]

    def ls_slicing_negative(self):
        result1 = self.num_list[-4:]  # index -4(7) 부터 마지막 까지 : [7, 8, 9, 10]
        result2 = self.num_list[:-4]  # 처음부터 index -4(7) 전(6)까지 : [1, 2, 3, 4, 5, 6]

    def ls_slicing_reverse(self):
        # index 상 역순으로 slicing 하기 위해서는, step 이용 하지 않으면 빈 배열인 [] 임
        # ex) num_list[-2:-4]
        # ex) num_list[4:2]
        result1 = self.num_list[::-3]  # 맨 마지막부터 역순으로 3개씩 건너 뛰면서 : [10, 7, 4, 1]
        result2 = self.num_list[2:-2:2]  # index 2 부터, index -2(9) 전(8)까지 2칸씩 : [3, 5, 7]


# BOOKMARK <#6> : [LIST] 배열 내 탐색 - 특정 값 index 찾기
class ListSearching:
    def __init__(self):
        self.num_list = [1, 2, 3, 1, 5, 3, 7, 8, 10]

    def ls_function_index(self, value):
        # list 내에 찾으려는 값의 index를 return 하며, 해당 값이 없으면 오류인 ValueError 발생
        try:
            value_idx = self.num_list.index(value)
            return value_idx
        except Exception as e:
            print(f'error : {e}, list 내 value 에 해당되는 값이 존재하지 않음')

    def ls_function_find(self, value, start, end):
        # AttributeError: 'list' object has no attribute 'find' -> list는 find를 지원하지 않기 때문에,
        # list 를 str 로 변형 시킨 후에 이용해야 하며.
        num_list_to_str = ''.join(map(str, self.num_list))
        value_idx = num_list_to_str.find(str(value), start, end)

        # 찾으려는 value 또한 int 형이 아닌, str 형으로 받아줘야 한다.(혹시 int로 받더라도 str로 다시 그냥 변형시키기)
        # start, end 는 생략 가능하며 (start) ~ (end-1) 까지 value 값이 있는지 확인한다.

        return value_idx

    def ls_function_count(self, value, start, end):
        # list 내에 value 에 해당되는 값이 몇개인지 return
        # count 도 범위 내에 하고 싶다면, list 자체에 slicing 을 적용하자.
        num_count = self.num_list[start:end].count(value)
        return num_count

    def ls_search_indices(self, value):
        # count 함수는 갯수만 return 하기 때문에, 각각 index 를 return 하도록 함
        value_indices = [i for i, j in enumerate(self.num_list) if j == value]

        # 찾고 난 후, len 함수를 이용하면 개수도 동시에 구할 수 있음
        num_count = len(value_indices)

        print(f'{value}는 리스트 안에 {num_count}개, {value_indices}에 있다.')

        return value_indices


# BOOKMARK <#7> : [LIST] 중복 제거
class ListRemoveDuplicates:
    def __init__(self):
        self.num_list = [1, 10, 1, 10, 1, 10, 2, 3, 5, 7, 8, 2, 8]

    def lrd_ascending(self):
        # 중복 제거 후 오름차순으로 정렬 됨
        # new_num_list => [1, 2, 3, 5, 7, 8, 10]
        new_num_list = list(set(self.num_list))
        return new_num_list

    def lrd_original(self):
        # 중복 제거를 하더라도 순서는 그대로 함
        # new_num_list => [1, 10, 2, 3, 5, 7, 8]
        new_num_list = list(dict.fromkeys(self.num_list))
        return new_num_list

    def lrd_original2(self):
        # 위 함수와 결과값은 같지만, 반복문을 사용
        new_num_list = []
        for num in self.num_list:
            if num not in new_num_list:
                new_num_list.append(num)

        return new_num_list