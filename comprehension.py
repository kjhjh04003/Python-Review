def list_comprehension():
    """ 리스트 내포
    Syntax : [표현식 for 변수 in 수치형 if 조건식] """
    # 1~10까지의 리스트가 있을 때, 내부 항복을 제곱한 새로운 리스트 생성
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [] # 제곱한 새로운 값 넣을 리스트

    # 기본 for 형식
    for num in nums:
        rst = num * num
        res.append(rst)
    print("결과 : ", res)

    # 리스트 내포 버전
    res = [num*num for num in nums]
    print("내포 결과 : ", res)

    # strings의 요소 중에서 문자열 길이가 3이하인 문자열 리스트 생성
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    res = []

    # 기본 for 형식
    for item in strings:
        if len(item) <= 3:
            res.append(item)
    print("for 결과 : ", res)

    # list 내포
    res = [item for item in strings if len(item) <= 3]
    print("내포 결과 : ", res)

    # 1~100까지 수 중에서 짝수의리슽트 생성
    evens = [i for i in range(1, 101) if i % 2 == 0]
    print("짝수 : ", evens)

def set_comprehension():
    # Syntax : {표현식 for 변수 in 순차형 if 조건}
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

    # strings의 요소 중에서 문자열 길이가 3이하인 문자열 set 생성
    res = {item for item in strings if len(item) <= 3}
    print(res, type(res))

    # strings의 요소 문자열 길이를 set으로 저장
    res = {len(item) for item in strings}
    print(res)

def dict_comprehension():
    # Syntax : {키표현식 : 값표현식 for 변수 in 순차형 if 조건문}
    # strings의 값 = 키, 값의 길이 = 값으로 받는 새로운 dict 생성
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    dct = {item:len(item) for item in strings}
    print(dct)



if __name__ == "__main__":
    # list_comprehension()
    # set_comprehension()
    dict_comprehension()