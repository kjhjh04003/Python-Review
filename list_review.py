""" 리스트정의 연습 """
def define_list():
    lst1 = list() # 빈 리스트
    print(lst1, type(lst1))
    lst2 = []
    lst3 = [1, 2, "python"]
    print(lst2, lst3)
    lst4 = list("Python") # 다른 시퀀스 객체를 리스트로 반환
    print(lst4, type(lst4))

""" 리스트 연산 
순차형의 모든 기능을 수행
immutable -> 내부 데이터 변경 가능 """
def list_oper():
    lst = [1, 2, "Python"]

    # 길이 확인
    print(lst, "length : ", len(lst))

    # 인덱싱
    print(lst[0], lst[1], lst[2]) # 정인덱싱
    print(lst[-3], lst[-2], lst[-1]) # 역인덱싱

    # 슬라이싱(Slicing)
    print(lst[1:3])
    print(lst[1:])
    print(lst[:3])
    print(lst[:])
    print("======================")

    copy = lst[:] # 슬라이싱을 이용한 리스트 전체 복사
    print(copy)
    print(copy is lst) # False -> 슬라이싱을 이용한 복사 -> 새 객체가 생성된다.

    # 연결(+) -> 원본을 변경시키지 않고 단순히 두 리스트를 연결한 새 리스트를 반환
    # append, extend -> 두 리스트를 합쳐 원본을 변경시킨다.
    print(lst + ["Java", True, 3.14159])
    print("원본 : ", lst)

    # append vs extend
    copy.append(["Java", True, 3.14159]) # 전달받은 요소 전체가 다음 인덱스에 저장
    print(copy)
    copy.extend(["Java", True, 3.14159]) # 전달받은 요소를 개별로 인덱스에 저장
    print(copy)

    # insert(인덱스, 저장하고싶은 리스트)
    copy.insert(2, [1, 2, 3]) # 삽입하고 싶은 요소 전체를 원하는 인덱스 자리에 저장
    print(copy)

    # 반복(*)
    print("원본 : ", lst)
    print("반복 : ", lst*3)

    # 포함여부 확인, in / not in
    print("Python" in lst) # False -> 대소문자를 구분하여 lst에 Python이 있는지 확인

    # 인덱스 확인 -> 해당 데이터가 리스트에 없다면 오류 발생
    # print("Index : ", lst.index("Python"))
    # 오류발생하지 않게 판별
    if "Python" in lst:
        print("Index : ", lst.index("Python"))
    else:
        print("리스트에 없음")

    # 항목 갯수
    print(copy)
    print("COUNT : ", copy.count("Python"))

    # 삭제 : del
    del copy[0] # copy의 0번 인덱스 요소 삭제
    print(copy)

    # 삭제 : remove
    copy.remove(3.14159)
    print(copy)

    # 슬라이싱을 이용한 치환
    # 메서드 이용보다 슬라이싱을 이용한 치환 방법을 먼저 이용하는 것을 권장
    print("======================")
    lst = [1, 12, 123, 1234, 12345]
    print("원본 : ", lst)
    lst[0:2] = [10, 20]
    print(lst)

    # 슬라이싱을 이용한 삭제
    lst[0:2] = [] # 슬라이싱 범위에 빈 리스트를 할당
    print(lst)

    # 슬라이싱을 이용한 삽입
    # lst[1:1] = 'inserted' # 각 개별 요소로 삽입
    lst[1:1] = ['inserted']
    print(lst)

    # 맨 마지막에 삽입
    lst[4:] = ["appended"]
    print(lst)

    # 맨 앞에 삽입
    lst[:0] = ['prepended']
    print(lst)

    # 다양한 기초 산술 함수 제공
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUM : ", sum(lst))
    print("MIN : ", min(lst))
    print("MAX : ", max(lst))
    print("AVG : ", sum(lst)/len(lst)) # 평균 함수는 없다.

""" 리스트 메서드 """
def list_methods():
    lst = [10, 2, 22, 9, 8, 33, 4, 12]
    print("원본 : ", lst)

    # 복제 메서드 : copy()
    copy = lst.copy()
    print("복제 : ", copy) # 원본 리스트가 변경된다.

    # 리스트 반전 : reverse()
    copy.reverse()
    print("반전 : ", copy)

    print("================================")
    copy = lst.copy()
    print(copy)

    # 정렬 : sort()
    # 메서드로서의 sort : 실제 내부 데이터가 sort
    # 문법적으로의 sorted : 정렬된 새 리스트 반환
    # sorted
    result = sorted(copy) # 기본 오름차순
    print("sorted 정렬 : ", result)
    result = sorted(copy, reverse=True) # 내림차순 정렬
    print(result)

    # sorted의 정렬 키 전달 -> 정렬 키를 기준으로 정렬
    print("================================")
    print("원본 : ", copy)
    rst = sorted(copy, key = str) # key 함수를 이용하여 정렬 기준을 str로 변경
    print(rst)

    # 사용자정의 정렬키 만들기
    # 리스트의 요소를 5로 나눈 나머지의 역순으로 정렬
    # 리스트의 요소를 5로 나눈 나머지가 키가 된다.
    def key_func(val): # 사용자 정의 키 생성 함수
        return val % 5
    rst = sorted(copy, key=key_func, reverse=True)
    print(rst)
    print("원본 : ", copy)

    # sort() 메서드 : 원본 배열 재정렬되어 저장
    copy.sort(key=key_func, reverse=True)
    print(copy)

""" 리스트를 이용한 스택 구현
append, pop 메서드를 이용
Last in First out """
def stack_ex():
    stack = []

    # 입력
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("stack : ", stack)

    # 인출
    print("pop : ", stack.pop())
    print("pop : ", stack.pop())
    print("pop : ", stack.pop())
    # print("pop : ", stack.pop()) # 스택이 비어있는데 인출하려고 하면 indexError 오류발생
    # 오류 방지 코드
    if len(stack) : # 스택이비어있지 않으면
        print("pop : ", stack.pop())
    else:
        print("스택이 비었습니다.")

""" 리스트를 이용한 큐의 구현
append, pop을 이용
First in First out """
def queue_ex():
    queue = []

    # 입력
    queue.append(10)
    queue.append(20)
    queue.append(30)
    print("queue : ", queue)

    # 인출
    print("pop : ", queue.pop(0))
    print("pop : ", queue.pop(0))
    print("pop : ", queue.pop(0))
    # print("pop : ", queue.pop(0)) # 큐가 비어있는데 인출하려하면 IndexError 오류 발생
    # 오류 방지 코드
    if len(queue):
        print("pop : ", queue.pop(0))
    else:
        print("큐가 비었습니다.")

"""  리스트 순회(반복) """
def loop():
    words = "Life is to short, you need Python".replace(",","").upper().split()
    print(words)

    for word in words:
        print(word)

if __name__ == "__main__":
    # define_list()
    # list_oper()
    # list_methods()
    # stack_ex()
    # queue_ex()
    loop()