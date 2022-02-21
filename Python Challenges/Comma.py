#No.11
#숫자를 입력받고, 숫자 3자리마다 콤마를 찍어 출력하는 프로그램을 작성해주세요.

#조건 1 : 4자리 미만의 숫자라면 콤마를 찍지 않습니다.
#조건 2 : 숫자의 길이는 20을 넘지 않습니다.

num = input("숫자를 입력하세요: ")
if len(num) < 4:
    print(num)
elif len(num) < 20:
    print(format(int(num), ","))
else:
    print("숫자가 너무 큽니다. 프로그램을 종료합니다.")

help('FORMATTING')