# 랜덤 임포트
import random

dollimpan = [] # 돌림판 리스트 생성

def main(): # 메인 함수
    print("돌리기 / 설정 / 종료")
    a = input()
    if a == "돌리기":
        run() # '돌리기' 입력하면 run 함수 실행
    if a == "설정":
        option() # '설정' 입력하면 option 함수 실행
    if a == "종료":
        exit() # '종료' 입력하면 exit 함수 실행
    else:
        print("유효하지 않은 입력값입니다.")
        main() # 유효하지 않은 입력값 입력시 출력되는 문구

def run():
    print("추가하고 싶은 항목을 입력한 후 Enter를 누르세요. ￦n얼마든지 추가할 수 있습니다. ￦n추가가 끝나면 '돌리기'를 입력하세요.")
    dollimpan_input = input() # 항목 입력받기
    if dollimpan_input != '돌리기': 
        dollimpan.append(dollimpan_input) # dollimpan 리스트에 입력값 추가
    if dollimpan_input == '돌리기':
        if len(dollimpan) != 0: # dollimpan 리스트에 값이 있을 때 실행
            dollimpan_max = len(dollimpan) - 1 # dollimpan_max에 최대 인덱스 값 설정
            pick = random.randint(0, dollimpan_max) # pick에 랜덤 인덱스 값 설정
            print("돌림판의 결과는...")
            print(dollimpan[pick]) # 돌림판 결과 출력
            # again() # 다시 시작 함수 실행
        if len(dollimpan) == 0: # dollimpan 리스트에 값이 없을 때 실행
            print("돌림판에 아무것도 없습니다.")

def option():
    pass # 설정 함수 (추가 기능 구현 예정)

main()