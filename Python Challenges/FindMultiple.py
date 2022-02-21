#공백으로 구분된 문자열 형태의 두 숫자를 입력받고, 

#n을 입력받아 두 숫자 사이에 존재하는 n의 배수를 구해보세요.
#조건 1 : 숫자 두 개는 공백(스페이스 바)로 구분되어 입력됩니다.
#조건 2 : 숫자 두 개는 문자열 형태로 입력됩니다.
#조건 3 : 입력된 숫자를 포함하여 배수를 출력해보세요.

num1, num2 = list(map(int, input("숫자 두 개를 입력해주세요(ex. '3 5'): ").split()))
find_mul = int(input("배수를 알고 싶은 숫자를 입력해주세요: "))

mul_list = []
for i in range(num1, num2+1):
    if i % find_mul == 0:
        mul_list.append(i)

for element in mul_list:
    print(element, end= ' ')