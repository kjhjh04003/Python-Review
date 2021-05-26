def define_tuple():
    """ 튜플 정의 연습 """
    tp = tuple()
    print(tp, type(tp))

    # 캐스팅 : 다른 순차 자료형을 기반으로 튜플 생성
    tp = tuple({1, 3, 5, 7, 9})
    print(tp, type(tp))

    tp = () # 빈 튜플 생성
    tp2 = (1,) # 1개 요소만 추가할 때에는 반드시 콤마 추가
    tp3 = (1, 2, 3)
    print(tp, tp2, tp3)

def tuple_oer():
    """ 튜플의 연산
    대부분 리스트와 비슷
    immutable 자료형 -> len, 인덱싱, 슬라이싱, 포함여부 확인 가능
                    -> 슬라이싱을 이용한 치환은 불가
                    -> 메서드 한정적 """
    tp = (1, 2, 3, 4, 5)

    # 길이
    print(tp, "len : ", len(tp))

    # 인덱싱 접근 가능
    print("정인덱싱 : ", tp[0], tp[1], tp[2], tp[3], tp[4])
    print("역인덱싱 : ", tp[-5], tp[-4], tp[-3], tp[-2], tp[-1])

    # tp[3] = 0 # tuple은 immutable 자료형이기 때문에 오류 발생

    # 연결(+)
    print(tp + (6, 7, 8))
    print(tp)

    # 반복(*)
    print(tp*3)

    # 포함 여부
    print(3 in tp)
    print(3 not in tp)

def tuple_method():
    """ 메서드가 많지 않다. """
    tp = (20, 30, 10, 20)

    # 검색 : index
    print("1st 20 : ", tp.index(20))
    print("2st 20 : ", tp.index(20, 1)) # 검색 범위 제한

    # 요소 갯수 확인
    print("count : ", tp.count(20))

def packing_unpacking():
    """ 튜플의 패킹 & 언패킹 """
    tp = (10, 20, 30, "Python")
    print(tp, type(tp))
    tp = 10, 20, 30, "Python" # () 명시하지 않아도 튜플로 인식 -> packing
    print(tp, type(tp))

    # 기본 unpacking
    (a, b, c, d) = tp
    print(a, b, c, d)
    a, b, c, d = tp
    print(a, b, c, d)

    # 좌변 변수 갯수와 우변 변수 갯수가 일치하지 않으면 ValuesError 발생
    # a, b, c = tp # 좌변의 변수 갯수가 우변의 튜플의 갯수보다 작기 때문에 오류 발생
    # a, b, c, d, e = tp # 좌변의 변수 갯수가 우변의 튜플 갯수보다 많기 때문에 오류 발생

    # 확장 언패킹
    # 지정되지 않은 갯수의 요소 변수 앞에 *
    a, *b = tp
    print("a : ", a, "b : ", b) # 지정되지 않은 갯수가 들어가는 변수의 타입은 list

    *a, b = tp
    print("a : ", a, "b : ", b)

    a, *b, c = tp
    print("a : ", a, "b : ", b, "c : ", c)





if __name__ == "__main__":
    # define_tuple()
    # tuple_oer()
    # tuple_method()
    packing_unpacking()