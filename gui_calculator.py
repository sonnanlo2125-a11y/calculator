import tkinter as tk

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
    """계산 결과를 출력하고 기록에 추가하는 함수"""
    try:
        expression = display.get()
        result = eval(expression)
        
        # 계산 기록에 추가
        history_listbox.insert(0, f"{expression} = {result}")
        
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "오류")

# 메인 윈도우 생성
root = tk.Tk()
root.title("GUI 계산기")
root.geometry("600x400") # 창 크기 넓힘

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

# 버튼 정의
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# 버튼 생성 및 배치
row, col = 0, 0
for button_text in buttons:
    if button_text == '=':
        btn = tk.Button(button_frame, text=button_text, font=('Arial', 18), width=5, height=2, command=calculate_result)
    else:
        # 람다 함수를 사용하여 버튼 클릭 시 현재 버튼의 텍스트를 전달
        btn = tk.Button(button_frame, text=button_text, font=('Arial', 18), width=5, height=2, command=lambda char=button_text: on_button_click(char))
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 클리어 버튼
clear_button = tk.Button(button_frame, text='C', font=('Arial', 18), width=5, height=2, command=clear_display)
clear_button.grid(row=row, column=col, padx=5, pady=5)

# 계산 기록 프레임
history_frame = tk.Frame(main_frame, bd=2, relief=tk.SOLID)
history_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

history_label = tk.Label(history_frame, text="계산 기록", font=('Arial', 16))
history_label.pack(pady=10)

history_listbox = tk.Listbox(history_frame, font=('Arial', 12), height=15)
history_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

scrollbar = tk.Scrollbar(history_frame, orient=tk.VERTICAL, command=history_listbox.yview)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

history_listbox.config(yscrollcommand=scrollbar.set)

# GUI 실행
root.mainloop()