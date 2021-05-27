# 글로벌 변수 선언
global_a = 1
global_b = "GLOBAL SCOPE"

# 사용자 정의 객체
class Myclass:
    x = 10
    y = 20

# 사용자 정의 함수
def func():
    # 로컬 변수 선언
    local_a = 2
    local_b = "LOCAL SCOPE"

    # 로컬 심볼 테이블 확인
    print(locals())
    print(type(locals()))

# 심볼 테이블 확인
def symbol_table():
    # 글로벌 심볼 테이블
    print(globals())
    print(type(globals()))

    # 심볼테이블은 객체의 심볼과 객체의 id를 담고 있는 dict이다.
    print("global_a : ", globals().get("global_a"))
    print("global_b : ", globals().get("global_b"))

    func()

    # 객체 내부의 __dict__ 속성을 확인하면 객체 내부의 심볼 테이블을 확인할 수 있다.
    # 1. 정의된 함수 객체 내부의 심볼 테이블 확인
    func.dynamic = "Hello"
    print(func.__dict__)

    # 2. 클래스 객체 내부의 심볼 테이블 확인
    print(Myclass.__dict__) # 사용자 정의 클래스의 심볼 테이블
    print(int.__dict__) # 내장 정의 클래스의 심볼 테이블

def ref_count():
    """ 참조 카운트 """
    x = object()
    print(x, type(x))

    # 참조 카운트 확인
    import sys # system 모듈 임포트
    print("refcount : ", sys.getrefcount(x))

    y = x # y에 x의 참조 주소를 복사
    print("refcount : ", sys.getrefcount(y))

    # x의 참조를 삭제
    del x
    print("refcount : ", sys.getrefcount(y))

    # 참조 카운트가 0인 객체 발견 -> garbage collection 작업 수행

def object_id():
    """ 객체 ID : 객체 ID는 참조 주소 """
    # 불변 자료형 : 두 값이 같으면 같은 객체이다.
    i1 = 10
    i2 = int(10)
    print("int : ", hex(id(i1)), hex(id(i2)))

    # 가변 자료형 : 두 값이 같아도 같은 객체가 아니다.
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("list : ", hex(id(lst1)), hex(id(lst2)))

    # 참조 복사 : 객체 주소 복사 -> 같은 객체
    lst3 = lst2
    print("참조 복사 : ", hex(id(lst2)), hex(id(lst3)))

    # ==는 동등성의 비교(값이 같은지), is는 동일성 비교(같은 객체인지)
    print("불변객체 비교 : ", i1 == i2, i1 is i2)
    print("가변객체 비교 : ", lst1 == lst2, lst1 is lst2)
    print("참조복사 비교 : ", lst2 == lst3, lst2 is lst3)

def object_copy():
    """ 객체 복제 """
    import copy

    # 래퍼런스 복사 : 객체의 주소값만 복사 -> 같은 객체가 된다.
    a = 1
    b = a
    print("a is b? ", a is b)

    # 얕은 복제 : 객체는 다르지만 내부 요소는 같다.
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]
    print("a : ", a)
    print("b : ", b)
    print("x : ", x)

    y = x # 레퍼런스 복사
    print("x is y? ", x is y)
    x[0][2] = 10
    print("x : ", x)
    print("y : ", y)

    y = copy.copy(x) # 얕은 복사, 객체는 다르지만 내부 요소는 같다.
    print("얕은 복제 : x is y? ", x is y)
    print("x : ", x)
    print("y : ", y)
    print("x == y? ", x == y)
    x[0][2] = 3
    print("x : ", x)
    print("y : ", y)
    print(x is y)
    print("x[0] is y[0]? ", x[0] is y[0])

    # deepcopy(깊은 복제)
    # 가장 하위의 요소로부터 복제해서 새 객체를 (재귀적으로)만들어서 객체를 재구성
    y = copy.deepcopy(x)
    print("x is y? ", x is y)
    print("x[0] is y[0]? ", x[0] is y[0])
    print("x[1] is y[1]? ", x[1] is y[1])

    x[0][2] = 20
    print("x : ", x)
    print("y : ", y)

if __name__ == "__main__":
    # func()
    # symbol_table()
    # ref_count()
    # object_id()
    object_copy()