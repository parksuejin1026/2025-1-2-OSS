🐍 파이썬 기초 개념 정리
1. 변수 (Variables)
변수는 데이터를 저장하는 이름표입니다. 등호(=)를 사용해 값을 할당합니다. 파이썬은 변수에 저장되는 데이터의 종류(자료형)를 자동으로 파악합니다.

Python

# 변수 선언 및 값 할당
age = 30
name = "Alice"
is_student = True

# 변수의 값 출력
print(name)
2. 자료형 (Data Types)
데이터의 종류를 의미합니다. 파이썬의 주요 자료형은 다음과 같습니다.

기본 자료형:

정수 (int): 소수점이 없는 숫자. 10, -5

실수 (float): 소수점이 있는 숫자. 3.14, 2.0

문자열 (str): 문자의 나열. 따옴표로 묶음. "Hello", 'Python'

논리형 (bool): 참(True) 또는 거짓(False).

컬렉션 자료형:

리스트 (list): 순서가 있고 변경 가능한 객체의 집합. [1, 'a', 3.14]

딕셔너리 (dict): **키(key)**와 **값(value)**의 쌍. {'name': 'Bob', 'age': 25}

3. 조건문 (Conditional Statements)
특정 조건에 따라 다른 코드를 실행할 때 사용합니다. if, elif(else if), else 키워드를 사용합니다.

Python

score = 85

if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
else:
    print("C 학점")
4. 반복문 (Loops)
코드를 반복해서 실행합니다. for와 while 반복문이 있습니다.

for 반복문: 리스트, 문자열 등 반복 가능한 객체의 요소를 하나씩 꺼내면서 반복합니다.

Python

for i in range(3):  # 0, 1, 2 출력
    print(i)
while 반복문: 주어진 조건이 참(True)인 동안 코드를 반복해서 실행합니다.

Python

count = 0
while count < 3:
    print(count)
    count += 1
5. 함수 (Functions)
특정 작업을 수행하는 코드 묶음입니다. 코드를 재사용하고 효율적으로 관리하는 데 도움이 됩니다. def 키워드로 정의하고, 정의된 함수는 호출하여 사용합니다.

Python

def greet(name):
    # 이 부분은 함수의 본문입니다.
    print(f"안녕하세요, {name}님!")

# 함수 호출
greet("Python")