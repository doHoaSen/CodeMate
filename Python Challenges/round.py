#파이썬에 내장된 round() 함수 이용하지 않고 반올림 계산 실행할 수 있는 코드
#조건1 : 소수 첫째자리에서 반올림
#조건2: 소수 첫째자리가 0~4이면 버림, 5~9이면 올림


def upper(n):
    num_int = int(n)
    print(num_int + 1)


def lower(n):
    num_int = int(n)
    print(num_int)


def make_round(n): 
    num_int = int(n)
    num_con = n - num_int

    if num_con <= 0.4:
        round_num = num_int
        print(round_num)
    else:
        round_num = num_int + 1
        print(round_num)



#main
check = True
while check:
    option = int(input("원하는 기능을 선택하세요 [1: 올림 2: 버림 3: 반올림 4: 종료]: "))
    if option == 4:
        print("프로그램을 종료합니다.")
        break
    
    usernum = float(input("원하는 수를 입력하세요: "))
    if option == 1:
        upper(usernum)
    elif option == 2:
        lower(usernum)
    elif option == 3:
        make_round(usernum)
    else: 
        print("잘못된 수를 입력했습니다. 다시 시도해주세요.")


