# 공백으로 구분된 자연수를 입력받은 후, 각 입력된 숫자들 중 자릿수의 합이 가장 큰 수를 구해보세요.
# (713의 자릿수의 합) = 7 + 1 + 3 = 11 / (112의 자릿수의 합) = 1 + 1+ 2 = 4
# 조건 1 : 각 숫자들은 공백(스페이스 바)로 구분되어 입력됩니다.
# 조건 2 : 숫자 두 개는 문자열 형태로 입력됩니다.

num_list = list(input("각 숫자를 공백으로 구분하여 입력하세요: ").split(" "))
#print(num_list)
sum_digit_dict = {}


for num in num_list:
    sum_digit = 0
    for char in num:
        sum_digit += int(char)
        #print(sum_digit)
    sum_digit_dict[num] = sum_digit

print(max(sum_digit_dict))