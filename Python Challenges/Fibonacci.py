#숫자 n을 입력받아 피보나치 수열의 n번째 숫자를 출력하는 프로그램을 작성해보세요.

#조건 1 : 입력받는 숫자 n은 2 이상의 자연수입니다.
#조건 2 : n > 2인 피보나치 수에서, n번째 수 = (n - 2)번째 수 + (n - 1)번째 수 입니다.
#조건 3 : 피보나치 수열을 나열하면 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 입니다.

#Find fibonacci number using list
# def fibonacci(n):
#     fib_list = [0]
#     n = 0
#     for i in range(1, 100):
#         if i < 3:
#             n = 1
#             fib_list.append(n)
#         else:
#             n = fib_list[i-2] + fib_list[i-1]
#             fib_list.append(n)
    #print(fib_list)


#Find fibonacci numbers using recursion
def fibonacci(num):
    if num < 3:
        return 1
    return fibonacci(num-2) + fibonacci(num-1)


#main
again = True
while again == True:
    num = int(input("2 이상의 숫자를 입력하세요: "))
    if num < 2:
        num = int(input("2 이상의 숫자를 다시 입력하세요: "))
    else:
        print(fibonacci(num))
        again = False
