import tkinter as tk
import math

def on_button_click(char):
    """버튼 클릭 시 호출되는 함수"""
    current_text = display.get()
    if current_text == "오류":
        clear_display()
        current_text = ""
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(char))

def clear_display():
    """입력창을 지우는 함수"""
    display.delete(0, tk.END)

def calculate_result():
    """
    입력된 표현식을 계산하고 결과를 출력합니다.
    공학용 연산을 위해 math 라이브러리를 사용합니다.
    """
    expression = display.get()
    try:
        # 사용자 친화적인 연산자를 Python 코드로 변환
        # 예: ^ -> **, log -> math.log10, ln -> math.log
        expression = expression.replace('^', '**')
        expression = expression.replace('√', 'math.sqrt')
        
        # 삼각함수와 로그 함수 매핑 (math 라이브러리 함수 사용)
        # eval() 함수 내에서 사용할 수 있도록 딕셔너리 정의
        allowed_functions = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "log": math.log10, "ln": math.log, "sqrt": math.sqrt,
            "pi": math.pi, "e": math.e
        }
        # 참고: math.sin, cos, tan은 라디안 값을 사용합니다.
        
        # eval() 함수를 안전하게 사용하여 표현식 계산
        result = eval(expression, {"__builtins__": None}, allowed_functions)
        
        # 계산 기록에 추가
        history_listbox.insert(0, f"{expression.replace('**', '^')} = {result}")
        
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "오류")

# --- GUI 설정 ---

# 메인 윈도우 생성
root = tk.Tk()
root.title("공학용 계산기")
root.geometry("800x600")

# 메인 프레임
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# 계산기 프레임
calculator_frame = tk.Frame(main_frame)
calculator_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# 결과 표시창
display = tk.Entry(calculator_frame, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
display.pack(padx=10, pady=20, fill='x')

# 버튼 프레임
button_frame = tk.Frame(calculator_frame)
button_frame.pack()

# 버튼 정의 (5열 구조)
buttons = [
    'sin', 'cos', 'tan', 'log', 'ln',
    '(',   ')',   '√',   '^',   '/',
    '7',   '8',   '9',   '*',   'C',
    '4',   '5',   '6',   '-',   'pi',
    '1',   '2',   '3',   '+',   'e',
    '0',   '.',   ''   , ''   , '' # 빈 공간을 위한 플레이스홀더
]

# 버튼 생성 및 배치
row, col = 0, 0
for button_text in buttons:
    if not button_text:  # 빈 텍스트는 건너뜀
        continue

    if button_text == 'C':
        cmd = clear_display
    else:
        cmd = lambda char=button_text: on_button_click(char)
    
    btn = tk.Button(button_frame, text=button_text, font=('Arial', 16), width=5, height=2, command=cmd)
    btn.grid(row=row, column=col, padx=3, pady=3)
    
    col += 1
    if col > 4:
        col = 0
        row += 1

# '=' 버튼은 넓게 만들기
equals_button = tk.Button(button_frame, text='=', font=('Arial', 16), width=11, height=2, command=calculate_result)
equals_button.grid(row=5, column=2, columnspan=2, padx=3, pady=3, sticky='we')


# --- 계산 기록 프레임 ---
history_frame = tk.Frame(main_frame, bd=2, relief=tk.SOLID)
history_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

history_label = tk.Label(history_frame, text="계산 기록", font=('Arial', 16))
history_label.pack(pady=10)

history_listbox = tk.Listbox(history_frame, font=('Arial', 12), height=15)
history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(history_frame, orient=tk.VERTICAL, command=history_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

history_listbox.config(yscrollcommand=scrollbar.set)

# GUI 실행
root.mainloop()