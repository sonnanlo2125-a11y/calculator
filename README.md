# Python 계산기 프로젝트 

이 저장소는 파이썬으로 만든 세 종류의 계산기 프로그램을 포함하고 있습니다. 각 파일은 점진적으로 기능이 확장되는 구조를 가집니다.

---

## 🚀 프로젝트 구성

### 1. `calculator.py`
- **설명:** 간단한 4칙 연산(+, -, *, /)을 수행하는 **커맨드 라인 기반**의 계산기입니다. 정수와 실수를 모두 입력받을 수 있습니다.
- **실행 방법:**
  ```shell
  python calculator.py
  ```

### 2. `gui_calculator.py`
- **설명:** 파이썬의 기본 GUI 라이브러리인 `tkinter`를 사용하여 만든 **GUI 계산기**입니다. 기본적인 4칙 연산과 함께, 계산했던 내역을 볼 수 있는 **기록(History) 기능**이 포함되어 있습니다.
- **실행 방법:**
  ```shell
  python gui_calculator.py
  ```

### 3. `scientific_calculator.py`
- **설명:** `gui_calculator.py`를 확장하여 삼각함수(sin, cos, tan), 로그(log, ln), 제곱근(√), 거듭제곱(^) 등 다양한 연산을 지원하는 **공학용 GUI 계산기**입니다. 계산 기록 기능도 동일하게 포함되어 있습니다.
- **실행 방법:**
  ```shell
  python scientific_calculator.py
  ```

---

## ✅ 요구 사항
- Python 3.x
- `tkinter` 라이브러리 (대부분의 파이썬 버전에 기본으로 내장되어 있습니다.)
