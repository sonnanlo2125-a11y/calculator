
def calculate(expression):
    """
    주어진 문자열 표현식을 계산합니다.
    예: "3+4", "5.5*2"
    """
    try:
        # 연산자 찾기
        op = None
        if '+' in expression:
            op = '+'
        elif '-' in expression:
            op = '-'
        elif '*' in expression:
            op = '*'
        elif '/' in expression:
            op = '/'
        
        if op is None:
            return "오류: 올바른 연산자(+, -, *, /)를 포함하여 입력해주세요."

        # 연산자를 기준으로 숫자 분리
        parts = expression.split(op)
        if len(parts) != 2:
            return "오류: '숫자 연산자 숫자' 형식으로 입력해주세요."

        num1 = float(parts[0])
        num2 = float(parts[1])

        # 계산 수행
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                return "오류: 0으로 나눌 수 없습니다."
            return num1 / num2

    except ValueError:
        return "오류: 숫자를 올바르게 입력해주세요."
    except Exception as e:
        return f"알 수 없는 오류가 발생했습니다: {e}"

def main():
    """
    메인 함수: 사용자 입력을 받아 계산기 실행
    """
    print("간단한 4칙연산 계산기입니다.")
    print("계산을 종료하려면 'exit'를 입력하세요.")
    
    while True:
        expression = input("계산식을 입력하세요 (예: 3+4): ")
        
        if expression.lower() == 'exit':
            print("계산기를 종료합니다.")
            break
            
        result = calculate(expression)
        print(f"결과: {result}")

if __name__ == "__main__":
    main()
