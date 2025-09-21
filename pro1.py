import random

def word_memorization():
    words = {}
    print("단어 암기 프로그램을 시작합니다. '종료'를 입력하여 프로그램을 종료하거나 '테스트'를 입력하여 암기 테스트를 시작할 수 있습니다.")
    
    while True:
        word = input("\n단어를 입력하세요 (종료/테스트): ")
        if word == '종료':
            print("프로그램을 종료합니다.")
            break
        if word == '테스트':
            if not words:
                print("먼저 단어를 추가해주세요.")
                continue
            
            test_words = list(words.keys())
            random.shuffle(test_words)
            
            correct_count = 0
            for w in test_words:
                answer = input(f"'{w}'의 뜻은 무엇인가요? ")
                if answer == words[w]:
                    print("정답입니다!")
                    correct_count += 1
                else:
                    print(f"오답입니다. 정답은 '{words[w]}'입니다.")
            
            print(f"\n테스트가 완료되었습니다. {len(test_words)}개 중 {correct_count}개를 맞혔습니다.")
            continue
            
        meaning = input(f"'{word}'의 뜻을 입력하세요: ")
        words[word] = meaning
        print(f"단어 '{word}'가 저장되었습니다.")

# 프로그램을 실행하려면 아래 주석을 해제하세요.
# word_memorization()

def quiz_generator():
    questions = [
        {"question": "파이썬에서 리스트를 만들 때 사용하는 기호는?", "answer": "["},
        {"question": "태양계에서 가장 큰 행성은?", "answer": "목성"},
        {"question": "대한민국의 수도는?", "answer": "서울"}
    ]
    
    score = 0
    for q in questions:
        print(f"\n문제: {q['question']}")
        user_answer = input("정답을 입력하세요: ")
        if user_answer == q['answer']:
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 '{q['answer']}'입니다.")
            
    print(f"\n퀴즈가 완료되었습니다. {len(questions)} 문제 중 {score}개를 맞혔습니다.")

# 프로그램을 실행하려면 아래 주석을 해제하세요.
# quiz_generator()

def simple_calculator():
    print("간단한 계산기입니다. '종료'를 입력하여 끝낼 수 있습니다.")
    
    while True:
        try:
            expression = input("계산식을 입력하세요 (예: 10 + 5): ")
            if expression == '종료':
                print("계산기를 종료합니다.")
                break
            
            # eval() 함수는 문자열로 된 파이썬 표현식을 실행합니다.
            result = eval(expression)
            print(f"결과: {result}")
        
        except Exception as e:
            print(f"잘못된 입력입니다: {e}")

# 프로그램을 실행하려면 아래 주석을 해제하세요.
# simple_calculator()
